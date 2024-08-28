import aio_pika

from .database import engine, SessionLocal
from fastapi import FastAPI, Depends, HTTPException, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from . import crud, models, schemas, database, rabbitmq, mongo
from .websocket_manager import manager

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Order Processing Service!"}

async def send_notification(order):
    connection = None
    try:
        connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
        channel = await connection.channel()

        # Declare a queue
        queue = await channel.declare_queue("order_notifications", durable=True)

        message_body = f"New order created with ID: {order.id}"

        await channel.default_exchange.publish(
            aio_pika.Message(body=message_body.encode()),
            routing_key=queue.name,
        )

        # Broadcast the message via WebSocket
        await manager.broadcast(message_body)

    except Exception as e:
        print(f"Failed to send notification: {e}")

    finally:
        if connection:
            await connection.close()

@app.websocket("/ws/notifications")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # This can be omitted if not needed
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("Client disconnected")


# Dependency for getting the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/orders/", response_model=schemas.OrderResponse)
async def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    # Create the order in PostgreSQL
    db_order = crud.create_order(db=db, order=order)

    # Log the order creation in MongoDB
    mongo.log_order_creation(db_order)

    # Send notification through RabbitMQ
    await rabbitmq.send_notification(db_order)

    return db_order

@app.get("/orders/{order_id}", response_model=schemas.OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db=db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.websocket("/ws/notifications")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # No need to receive messages from the client in this case
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("Client disconnected")

@app.get("/trigger-broadcast")
async def trigger_broadcast():
    await manager.broadcast("This is a test message")
    return {"message": "Broadcast sent"}
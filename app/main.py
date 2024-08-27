from fastapi import FastAPI
from . import models, schemas, crud
from .database import engine, SessionLocal
from .rabbitmq import send_notification

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)

@app.post("/orders/", response_model=schemas.OrderResponse)
async def create_order(order: schemas.OrderCreate):
    db = SessionLocal()
    db_order = crud.create_order(db=db, order=order)
    await send_notification(db_order)
    return db_order

@app.get("/orders/{order_id}", response_model=schemas.OrderResponse)
async def get_order(order_id: int):
    db = SessionLocal()
    return crud.get_order(db, order_id)

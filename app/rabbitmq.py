import aio_pika
import asyncio

async def send_notification(order):
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()

    # Declare a queue
    queue = await channel.declare_queue("order_notifications")

    message_body = f"New order created with ID: {order.id}"

    await channel.default_exchange.publish(
        aio_pika.Message(body=message_body.encode()),
        routing_key=queue.name,
    )

    await connection.close()

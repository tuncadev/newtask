import pika

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    print("RabbitMQ is running and accessible.")
    connection.close()
except Exception as e:
    print(f"Error: {e}")
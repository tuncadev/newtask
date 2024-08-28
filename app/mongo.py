from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.order_service_db

def log_order_creation(order):
    order_data = {
        "order_id": order.id,
        "product_id": order.product_id,
        "quantity": order.quantity,
        "client_name": order.client_name,
        "client_email": order.client_email,
        "status": order.status,
        "total_price": order.total_price
    }
    db.orders_history.insert_one(order_data)

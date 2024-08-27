from sqlalchemy.orm import Session
from . import models, schemas

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        product_id=order.product_id,
        quantity=order.quantity,
        client_name=order.client_name,
        client_email=order.client_email,
        total_price=calculate_total_price(order.product_id, order.quantity)
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def calculate_total_price(product_id: int, quantity: int) -> float:
    # Placeholder: Implement logic to fetch the product price and calculate total
    return 100.0 * quantity  # Example

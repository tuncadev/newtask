from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)
    quantity = Column(Integer)
    client_name = Column(String, index=True)
    client_email = Column(String, index=True)
    status = Column(String, default="Pending")
    total_price = Column(Float)

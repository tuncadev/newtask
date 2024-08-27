from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
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

    # You can add more fields like timestamps, etc.

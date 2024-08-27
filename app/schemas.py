from pydantic import BaseModel

class OrderCreate(BaseModel):
    product_id: int
    quantity: int
    client_name: str
    client_email: str

class OrderResponse(OrderCreate):
    id: int
    status: str
    total_price: float

    class Config:
        orm_mode = True

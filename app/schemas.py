from pydantic import field_validator, ConfigDict, BaseModel, EmailStr

class OrderCreate(BaseModel):
    product_id: int
    quantity: int
    client_name: str
    client_email: EmailStr

    @field_validator("quantity")
    def check_quantity(cls, value):
        if value <= 0:
            raise ValueError('Quantity must be greater than zero')
        return value

class OrderResponse(OrderCreate):
    id: int
    status: str
    total_price: float

    class Config:
        model_config = ConfigDict(from_attributes=True)

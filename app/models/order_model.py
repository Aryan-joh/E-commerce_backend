from pydantic import BaseModel, Field
from typing import List

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class Order(BaseModel):
    user_id: str
    items: List[OrderItem]
    total_amount: float
    shipping_address: str
    status: str = "pending"

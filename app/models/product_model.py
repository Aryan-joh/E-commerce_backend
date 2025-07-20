from pydantic import BaseModel
from bson import ObjectId
from typing import Optional

class Product(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class ProductInDB(Product):
    id: Optional[str]

    class Config:
        from_attributes = True

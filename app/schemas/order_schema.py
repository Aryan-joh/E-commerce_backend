from pydantic import BaseModel
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


# Serialize a single order
def order_serializer(order) -> dict:
    return {
        "id": str(order["_id"]),
        "user_id": order["user_id"],
        "items": [
            {
                "product_id": item["product_id"],
                "quantity": item["quantity"]
                # You can add product name or price here if needed
            }
            for item in order["items"]
        ],
        "total_amount": order["total_amount"],
        "shipping_address": order["shipping_address"],
        "status": order["status"]
    }


# Serialize list of orders
def order_list_serializer(orders) -> list:
    return [order_serializer(order) for order in orders]

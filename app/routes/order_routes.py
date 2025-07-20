from fastapi import APIRouter, HTTPException, Query, status
from bson import ObjectId
from app.database import db
from app.models.order_model import Order
from app.schemas.order_schema import order_serializer, order_list_serializer
from typing import List

router = APIRouter()
orders_collection = db["orders"]
products_collection = db["products"]

# Create order
@router.post("/", status_code=status.HTTP_201_CREATED, summary="Create a new order")
def create_order(order: Order):
    """
    Create a new order and return the created order.
    """
    result = orders_collection.insert_one(order.dict())
    created_order = orders_collection.find_one({"_id": result.inserted_id})
    
    if not created_order:
        raise HTTPException(status_code=500, detail="Order creation failed.")
    
    return {
        "status": "success",
        "message": "Order created successfully.",
        "order": order_serializer(created_order)
    }


# List orders by user with pagination
@router.get("/user/{user_id}", status_code=status.HTTP_200_OK, summary="List user's orders with pagination")
def get_orders_by_user(
    user_id: str,
    limit: int = Query(10, ge=1, le=100, description="Number of orders to retrieve"),
    offset: int = Query(0, ge=0, description="Number of orders to skip")
):
    """
    Get paginated orders placed by a specific user, including product details and totals.
    """
    orders_cursor = orders_collection.find({"user_id": user_id}).skip(offset).limit(limit)
    orders = list(orders_cursor)

    if not orders:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No orders found for this user.")

    for order in orders:
        for item in order.get("items", []):
            product = products_collection.find_one({"_id": ObjectId(item["product_id"])})
            if product:
                item["name"] = product.get("name")
                item["price"] = product.get("price")
                item["total_price"] = item["quantity"] * product.get("price", 0)

        order["total_amount"] = sum(
            item.get("total_price", 0) for item in order.get("items", [])
        )

    return {
        "status": "success",
        "message": "Orders retrieved successfully.",
        "user_id": user_id,
        "limit": limit,
        "offset": offset,
        "next": offset + limit,
        "previous": max(offset - limit, 0),
        "orders": order_list_serializer(orders)
    }

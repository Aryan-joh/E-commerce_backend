from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.database import db
from app.models.product_model import Product
from app.schemas.product_schema import product_serializer, product_list_serializer

router = APIRouter()
collection = db["products"]



@router.post("/", status_code=201)
def create_product(product: Product):
    result = collection.insert_one(product.dict())
    return {"id": str(result.inserted_id)}


@router.get("/{product_id}")
def get_product(product_id: str):
    product = collection.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_serializer(product)

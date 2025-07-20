from fastapi import FastAPI
from app.routes import product_routes, order_routes

app = FastAPI(
    title="Ecommerce API",
    description="API for managing products and orders",
    version="1.0.0"
)

app.include_router(product_routes.router, prefix="/products", tags=["Products"])
app.include_router(order_routes.router, prefix="/orders", tags=["Orders"])

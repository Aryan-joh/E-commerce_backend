from fastapi import FastAPI
from app.routes import product_routes, order_routes

app = FastAPI(
    title="Ecommerce API",
    description="API for managing products and orders",
    version="1.0.0"
)

# ✅ Root route
@app.get("/")
def read_root():
    return {
        "message": "Welcome to the E-commerce API."
    }

# ✅ Include routers
app.include_router(product_routes.router, prefix="/products", tags=["Products"])
app.include_router(order_routes.router, prefix="/orders", tags=["Orders"])

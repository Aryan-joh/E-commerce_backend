def product_serializer(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product["description"],
        "price": product["price"],
        "stock": product["stock"]
    }

def product_list_serializer(products) -> list:
    return [product_serializer(p) for p in products]

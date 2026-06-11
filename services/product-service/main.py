from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()

REQUESTS = Counter(
    "product_requests_total",
    "Total Product Requests"
)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 1200
    }
]

@app.get("/")
def root():
    REQUESTS.inc()
    return {"service": "product-service"}

@app.get("/products")
def get_products():
    REQUESTS.inc()
    return products

@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )
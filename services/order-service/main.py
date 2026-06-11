from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()

REQUESTS = Counter(
    "order_requests_total",
    "Total Order Requests"
)

orders = []

@app.get("/")
def root():
    REQUESTS.inc()
    return {"service": "order-service"}

@app.get("/orders")
def get_orders():
    REQUESTS.inc()
    return orders

@app.post("/orders")
def create_order(order: dict):
    REQUESTS.inc()
    orders.append(order)
    return {
        "message": "Order Created",
        "order": order
    }

@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )
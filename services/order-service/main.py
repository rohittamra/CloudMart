from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response
from kafka import KafkaProducer
import json

app = FastAPI()

REQUESTS = Counter(
    "order_requests_total",
    "Total Order Requests"
)

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v:
    json.dumps(v).encode("utf-8")
)

orders = []

@app.get("/")
def root():
    REQUESTS.inc()
    return {"service": "order-service"}

@app.post("/orders")
def create_order(order: dict):

    orders.append(order)

    producer.send(
        "order-created",
        order
    )

    producer.flush()

    return {
        "message": "Order Created",
        "order": order
    }

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
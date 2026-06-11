from fastapi import FastAPI
from kafka import KafkaConsumer
import threading
import json

app = FastAPI()

def consume():

    consumer = KafkaConsumer(
        "order-created",
        bootstrap_servers="kafka:9092",
        value_deserializer=lambda m: json.loads(m.decode())
    )

    for msg in consumer:

        print(
            f"Notification Service Received: {msg.value}"
        )

@app.on_event("startup")
def startup():

    thread = threading.Thread(
        target=consume,
        daemon=True
    )

    thread.start()

@app.get("/")
def root():
    return {
        "service": "notification-service"
    }
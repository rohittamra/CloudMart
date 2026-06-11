from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()

REQUESTS = Counter(
    "user_requests_total",
    "Total User Requests"
)

users = [
    {
        "id": 1,
        "name": "John"
    }
]

@app.get("/")
def root():
    REQUESTS.inc()
    return {"service": "user-service"}

@app.get("/users")
def get_users():
    REQUESTS.inc()
    return users

@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )
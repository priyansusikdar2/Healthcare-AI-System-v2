# backend/app/routers/delivery_router.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
delivery_db = []

class Delivery(BaseModel):
    patient_id: int
    service: str
    date: str

@router.post("/")
def add_delivery(delivery: Delivery):
    delivery_db.append(delivery.dict())
    return {"msg": "Delivery added", "delivery": delivery}

@router.get("/")
def get_deliveries():
    return {"deliveries": delivery_db}
# backend/app/routers/appointment_router.py
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

appointments_db = []

class Appointment(BaseModel):
    patient_id: int
    doctor_id: int
    date: datetime

@router.post("/")
def create_appointment(appointment: Appointment):
    appointments_db.append(appointment.dict())
    return {"msg": "Appointment created", "appointment": appointment}

@router.get("/")
def get_appointments():
    return {"appointments": appointments_db}
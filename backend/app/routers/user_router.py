# backend/app/routers/user_router.py
from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

# Dummy database
patients_db = []

class Patient(BaseModel):
    name: str
    age: int
    gender: str

@router.get("/patients")
def get_patients():
    return {"patients": patients_db}

@router.post("/")
def create_patient(patient: Patient):
    patients_db.append(patient.dict())
    return {"msg": "Patient added", "patient": patient}
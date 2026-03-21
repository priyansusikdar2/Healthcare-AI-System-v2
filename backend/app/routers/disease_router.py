# backend/app/routers/disease_router.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
disease_db = []

class DiseaseHistory(BaseModel):
    patient_id: int
    disease: str
    diagnosed_on: str

@router.post("/")
def add_disease(record: DiseaseHistory):
    disease_db.append(record.dict())
    return {"msg": "Disease record added", "record": record}

@router.get("/")
def get_disease_history():
    return {"disease_history": disease_db}
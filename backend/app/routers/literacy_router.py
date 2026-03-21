# backend/app/routers/literacy_router.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
literacy_db = []

class Literacy(BaseModel):
    patient_id: int
    literacy_score: int

@router.post("/")
def add_literacy(record: Literacy):
    literacy_db.append(record.dict())
    return {"msg": "Literacy record added", "record": record}

@router.get("/")
def get_literacy():
    return {"literacy_records": literacy_db}
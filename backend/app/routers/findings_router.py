# backend/app/routers/findings_router.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
findings_db = []

class Finding(BaseModel):
    patient_id: int
    finding: str

@router.post("/")
def add_finding(finding: Finding):
    findings_db.append(finding.dict())
    return {"msg": "Finding added", "finding": finding}

@router.get("/")
def get_findings():
    return {"findings": findings_db}
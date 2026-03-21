# backend/app/routers/engagement_router.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
engagements_db = []

class Engagement(BaseModel):
    patient_id: int
    activity: str

@router.post("/")
def add_engagement(engagement: Engagement):
    engagements_db.append(engagement.dict())
    return {"msg": "Engagement added", "engagement": engagement}

@router.get("/")
def get_engagements():
    return {"engagements": engagements_db}
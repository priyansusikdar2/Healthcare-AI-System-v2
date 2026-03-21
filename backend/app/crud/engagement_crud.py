from sqlalchemy.orm import Session
from typing import List
from backend.app.models import engagements
from app.schemas.engagement_schema import EngagementCreate, EngagementUpdate

def create_engagement(db: Session, engagement_obj: EngagementCreate):
    db_engagement = engagements.Engagement(**engagement_obj.dict())
    db.add(db_engagement)
    db.commit()
    db.refresh(db_engagement)
    return db_engagement

def get_engagement(db: Session, engagement_id: int):
    return db.query(engagements.Engagement).filter(engagements.Engagement.id == engagement_id).first()

def get_engagements(db: Session, skip: int = 0, limit: int = 100) -> List[engagements.Engagement]:
    return db.query(engagements.Engagement).offset(skip).limit(limit).all()

def update_engagement(db: Session, engagement_id: int, updates: EngagementUpdate):
    db_engagement = get_engagement(db, engagement_id)
    if db_engagement:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_engagement, key, value)
        db.commit()
        db.refresh(db_engagement)
    return db_engagement

def delete_engagement(db: Session, engagement_id: int):
    db_engagement = get_engagement(db, engagement_id)
    if db_engagement:
        db.delete(db_engagement)
        db.commit()
    return db_engagement
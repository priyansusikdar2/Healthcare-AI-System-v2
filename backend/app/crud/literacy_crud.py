from sqlalchemy.orm import Session
from typing import List
from app.models import health_literacy
from app.schemas.literacy_schema import HealthLiteracyCreate, HealthLiteracyUpdate

def create_literacy(db: Session, literacy_obj: HealthLiteracyCreate):
    db_lit = health_literacy.HealthLiteracy(**literacy_obj.dict())
    db.add(db_lit)
    db.commit()
    db.refresh(db_lit)
    return db_lit

def get_literacy(db: Session, literacy_id: int):
    return db.query(health_literacy.HealthLiteracy).filter(health_literacy.HealthLiteracy.id == literacy_id).first()

def get_literacies(db: Session, skip: int = 0, limit: int = 100) -> List[health_literacy.HealthLiteracy]:
    return db.query(health_literacy.HealthLiteracy).offset(skip).limit(limit).all()

def update_literacy(db: Session, literacy_id: int, updates: HealthLiteracyUpdate):
    db_lit = get_literacy(db, literacy_id)
    if db_lit:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_lit, key, value)
        db.commit()
        db.refresh(db_lit)
    return db_lit

def delete_literacy(db: Session, literacy_id: int):
    db_lit = get_literacy(db, literacy_id)
    if db_lit:
        db.delete(db_lit)
        db.commit()
    return db_lit
from sqlalchemy.orm import Session
from typing import List
from app.models import disease_history
from app.schemas.disease_schema import DiseaseHistoryCreate, DiseaseHistoryUpdate

def create_disease(db: Session, disease_obj: DiseaseHistoryCreate):
    db_dis = disease_history.DiseaseHistory(**disease_obj.dict())
    db.add(db_dis)
    db.commit()
    db.refresh(db_dis)
    return db_dis

def get_disease(db: Session, disease_id: int):
    return db.query(disease_history.DiseaseHistory).filter(disease_history.DiseaseHistory.id == disease_id).first()

def get_diseases(db: Session, skip: int = 0, limit: int = 100) -> List[disease_history.DiseaseHistory]:
    return db.query(disease_history.DiseaseHistory).offset(skip).limit(limit).all()

def update_disease(db: Session, disease_id: int, updates: DiseaseHistoryUpdate):
    db_dis = get_disease(db, disease_id)
    if db_dis:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_dis, key, value)
        db.commit()
        db.refresh(db_dis)
    return db_dis

def delete_disease(db: Session, disease_id: int):
    db_dis = get_disease(db, disease_id)
    if db_dis:
        db.delete(db_dis)
        db.commit()
    return db_dis
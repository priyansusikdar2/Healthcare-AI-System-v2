from sqlalchemy.orm import Session
from typing import List
from app.models import healthcare_delivery
from app.schemas.delivery_schema import HealthcareDeliveryCreate, HealthcareDeliveryUpdate

def create_delivery(db: Session, delivery: HealthcareDeliveryCreate):
    db_delivery = healthcare_delivery.HealthcareDelivery(**delivery.dict())
    db.add(db_delivery)
    db.commit()
    db.refresh(db_delivery)
    return db_delivery

def get_delivery(db: Session, delivery_id: int):
    return db.query(healthcare_delivery.HealthcareDelivery).filter(healthcare_delivery.HealthcareDelivery.id == delivery_id).first()

def get_deliveries(db: Session, skip: int = 0, limit: int = 100) -> List[healthcare_delivery.HealthcareDelivery]:
    return db.query(healthcare_delivery.HealthcareDelivery).offset(skip).limit(limit).all()

def update_delivery(db: Session, delivery_id: int, updates: HealthcareDeliveryUpdate):
    db_delivery = get_delivery(db, delivery_id)
    if db_delivery:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_delivery, key, value)
        db.commit()
        db.refresh(db_delivery)
    return db_delivery

def delete_delivery(db: Session, delivery_id: int):
    db_delivery = get_delivery(db, delivery_id)
    if db_delivery:
        db.delete(db_delivery)
        db.commit()
    return db_delivery
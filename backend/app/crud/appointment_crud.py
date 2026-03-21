from sqlalchemy.orm import Session
from typing import List
from app.models import appointment
from app.schemas.appointment_schema import AppointmentCreate, AppointmentUpdate

def create_appointment(db: Session, appt: AppointmentCreate):
    db_appt = appointment.Appointment(**appt.dict())
    db.add(db_appt)
    db.commit()
    db.refresh(db_appt)
    return db_appt

def get_appointment(db: Session, appt_id: int):
    return db.query(appointment.Appointment).filter(appointment.Appointment.id == appt_id).first()

def get_appointments(db: Session, skip: int = 0, limit: int = 100) -> List[appointment.Appointment]:
    return db.query(appointment.Appointment).offset(skip).limit(limit).all()

def update_appointment(db: Session, appt_id: int, updates: AppointmentUpdate):
    db_appt = get_appointment(db, appt_id)
    if db_appt:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_appt, key, value)
        db.commit()
        db.refresh(db_appt)
    return db_appt

def delete_appointment(db: Session, appt_id: int):
    db_appt = get_appointment(db, appt_id)
    if db_appt:
        db.delete(db_appt)
        db.commit()
    return db_appt
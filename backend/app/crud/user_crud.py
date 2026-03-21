from sqlalchemy.orm import Session
from typing import List
from app.models import user
from app.schemas.user_schema import PatientCreate, PatientUpdate, DoctorCreate, DoctorUpdate

# ------------------- Patients -------------------
def create_patient(db: Session, patient: PatientCreate):
    db_patient = user.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patient(db: Session, patient_id: int):
    return db.query(user.Patient).filter(user.Patient.id == patient_id).first()

def get_patients(db: Session, skip: int = 0, limit: int = 100) -> List[user.Patient]:
    return db.query(user.Patient).offset(skip).limit(limit).all()

def update_patient(db: Session, patient_id: int, updates: PatientUpdate):
    db_patient = get_patient(db, patient_id)
    if db_patient:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_patient, key, value)
        db.commit()
        db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int):
    db_patient = get_patient(db, patient_id)
    if db_patient:
        db.delete(db_patient)
        db.commit()
    return db_patient

# ------------------- Doctors -------------------
def create_doctor(db: Session, doctor: DoctorCreate):
    db_doctor = user.Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def get_doctor(db: Session, doctor_id: int):
    return db.query(user.Doctor).filter(user.Doctor.id == doctor_id).first()

def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user.Doctor).offset(skip).limit(limit).all()

def update_doctor(db: Session, doctor_id: int, updates: DoctorUpdate):
    db_doctor = get_doctor(db, doctor_id)
    if db_doctor:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_doctor, key, value)
        db.commit()
        db.refresh(db_doctor)
    return db_doctor

def delete_doctor(db: Session, doctor_id: int):
    db_doctor = get_doctor(db, doctor_id)
    if db_doctor:
        db.delete(db_doctor)
        db.commit()
    return db_doctor
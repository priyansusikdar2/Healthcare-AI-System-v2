from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class HealthcareDelivery(Base):
    __tablename__ = "healthcare_delivery"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer)
    service_name = Column(String)
    notes = Column(String)
    date_recorded = Column(DateTime, default=datetime.datetime.utcnow)

    patient = relationship("Patients", back_populates="healthcare_deliveries")
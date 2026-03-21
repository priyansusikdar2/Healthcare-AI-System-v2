from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class HealthLiteracy(Base):
    __tablename__ = "health_literacy"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    literacy_level = Column(String)
    notes = Column(String)
    date_recorded = Column(DateTime, default=datetime.datetime.utcnow)

    patient = relationship("Patients", back_populates="health_literacy")
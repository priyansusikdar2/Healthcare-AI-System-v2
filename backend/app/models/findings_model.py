from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class Findings(Base):
    __tablename__ = "findings"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer)
    finding_type = Column(String)
    description = Column(Text)
    notes = Column(Text)
    date_recorded = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationship
    patient = relationship("Patients", back_populates="findings")
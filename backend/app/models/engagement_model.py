from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class Engagements(Base):
    __tablename__ = "engagements"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer)
    engagement_type = Column(String)
    notes = Column(String)
    date_recorded = Column(DateTime, default=datetime.datetime.utcnow)

    patient = relationship("Patients", back_populates="engagements")
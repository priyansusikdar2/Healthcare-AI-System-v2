from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class DiseaseHistory(Base):
    __tablename__ = "disease_history"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    disease_name = Column(String, nullable=False)
    notes = Column(String)
    date_recorded = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationship
    patient = relationship("Patients", back_populates="disease_history")
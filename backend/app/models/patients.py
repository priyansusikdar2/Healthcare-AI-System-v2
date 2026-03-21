from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class Patients(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)
    contact = Column(String)
    email = Column(String)
    address = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Relationships
    findings = relationship("Findings", back_populates="patient", cascade="all, delete-orphan")
    disease_history = relationship("DiseaseHistory", back_populates="patient", cascade="all, delete-orphan")
    healthcare_deliveries = relationship("HealthcareDelivery", back_populates="patient", cascade="all, delete-orphan")
    engagements = relationship("Engagements", back_populates="patient", cascade="all, delete-orphan")
    health_literacy = relationship("HealthLiteracy", back_populates="patient", cascade="all, delete-orphan")
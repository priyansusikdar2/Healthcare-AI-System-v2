from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_time: datetime
    status: str = "scheduled"

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(BaseModel):
    appointment_time: Optional[datetime] = None
    status: Optional[str] = None

class AppointmentOut(AppointmentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
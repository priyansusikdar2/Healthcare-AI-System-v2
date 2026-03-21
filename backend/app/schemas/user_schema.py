from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Patient Schemas
class PatientBase(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None
    gender: Optional[str] = None
    phone: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    phone: Optional[str] = None

class PatientOut(PatientBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Doctor Schemas
class DoctorBase(BaseModel):
    name: str
    email: EmailStr
    specialization: Optional[str] = None
    phone: Optional[str] = None

class DoctorCreate(DoctorBase):
    pass

class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    phone: Optional[str] = None

class DoctorOut(DoctorBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
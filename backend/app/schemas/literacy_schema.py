from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HealthLiteracyBase(BaseModel):
    patient_id: int
    topic: str
    comprehension_level: Optional[str] = None
    notes: Optional[str] = None

class HealthLiteracyCreate(HealthLiteracyBase):
    pass

class HealthLiteracyUpdate(HealthLiteracyBase):
    pass

class HealthLiteracyOut(HealthLiteracyBase):
    id: int
    date_recorded: datetime

    model_config = {
        "from_attributes": True
    }
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FindingBase(BaseModel):
    patient_id: int
    doctor_id: int
    finding_type: str
    description: Optional[str] = None
    notes: Optional[str] = None

class FindingCreate(FindingBase):
    pass

class FindingUpdate(FindingBase):
    pass

class FindingOut(FindingBase):
    id: int
    date_recorded: datetime

    model_config = {
        "from_attributes": True
    }
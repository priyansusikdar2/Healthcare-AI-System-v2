from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EngagementBase(BaseModel):
    patient_id: int
    doctor_id: int
    engagement_type: str
    notes: Optional[str] = None

class EngagementCreate(EngagementBase):
    pass

class EngagementUpdate(EngagementBase):
    pass

class EngagementOut(EngagementBase):
    id: int
    date_recorded: datetime

    model_config = {
        "from_attributes": True
    }
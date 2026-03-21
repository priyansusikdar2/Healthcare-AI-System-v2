from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HealthcareDeliveryBase(BaseModel):
    patient_id: int
    doctor_id: int
    service_type: str
    notes: Optional[str] = None

class HealthcareDeliveryCreate(HealthcareDeliveryBase):
    pass

class HealthcareDeliveryUpdate(HealthcareDeliveryBase):
    pass

class HealthcareDeliveryOut(HealthcareDeliveryBase):
    id: int
    date_provided: datetime

    model_config = {
        "from_attributes": True
    }
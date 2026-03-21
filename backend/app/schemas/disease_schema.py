from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DiseaseHistoryBase(BaseModel):
    patient_id: int
    disease_name: str
    notes: Optional[str] = None

class DiseaseHistoryCreate(DiseaseHistoryBase):
    pass

class DiseaseHistoryUpdate(DiseaseHistoryBase):
    pass

class DiseaseHistoryOut(DiseaseHistoryBase):
    id: int
    date_recorded: datetime

    model_config = {
        "from_attributes": True
    }
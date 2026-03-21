from pydantic import BaseModel
from typing import Dict


# Input: symptom → value (0 or 1)
class PredictionInput(BaseModel):
    data: Dict[str, float]   # {"fever":1, "cough":0, ...}


# Output
class PredictionOutput(BaseModel):
    prediction: str
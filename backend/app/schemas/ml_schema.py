from pydantic import BaseModel, Field
from typing import Dict, Optional


# -----------------------------
# 🔥 REQUEST SCHEMA
# -----------------------------
class DiseasePredictionRequest(BaseModel):
    data: Dict[str, int] = Field(
        ...,
        description="Dictionary of symptoms with 0 or 1 values"
    )

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "itching": 1,
                    "skin_rash": 1,
                    "fatigue": 0,
                    "vomiting": 0
                }
            }
        }


# -----------------------------
# 🔥 RESPONSE SCHEMA (OPTIONAL BUT BEST PRACTICE)
# -----------------------------
class DiseasePredictionResponse(BaseModel):
    disease: Optional[str]
    confidence: Optional[float]
    error: Optional[str] = None
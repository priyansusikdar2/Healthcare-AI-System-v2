from fastapi import APIRouter
from ..schemas.prediction_schema import PredictionInput, PredictionOutput
from ..ml_model import predict_disease

router = APIRouter()


@router.post("/", response_model=PredictionOutput)
def predict(data: PredictionInput):
    """
    Input: dictionary of symptoms/features
    Output: predicted disease
    """
    prediction = predict_disease(data.data)
    return {"prediction": prediction}

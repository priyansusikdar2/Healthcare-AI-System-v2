from fastapi import APIRouter
from app.ml_model import predict_disease, feature_columns
from app.schemas.ml_schema import DiseasePredictionRequest

router = APIRouter()

# -----------------------------
# 🔥 PREDICT DISEASE
# -----------------------------
@router.post("/predict")
def predict(request: DiseasePredictionRequest):
    try:
        result = predict_disease(request.data)

        # If model returns error
        if "error" in result:
            return {
                "success": False,
                "error": result["error"]
            }

        # ✅ RETURN CLEAN FORMAT (MATCH STREAMLIT)
        return {
            "disease": result.get("disease"),
            "confidence": result.get("confidence")
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


# -----------------------------
# 🔥 GET ALL FEATURES (IMPORTANT)
# -----------------------------
@router.get("/features")
def get_features():
    try:
        return {
            "features": feature_columns
        }
    except Exception as e:
        return {
            "error": str(e)
        }
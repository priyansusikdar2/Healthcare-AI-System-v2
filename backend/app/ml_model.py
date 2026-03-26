import joblib
import os
import numpy as np

# -----------------------------
# PATH SETUP
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# -----------------------------
# LOAD FILES
# -----------------------------
try:
    metadata = joblib.load(os.path.join(MODEL_DIR, "model_metadata.pkl"))

    best_model_name = metadata["best_model"]
    use_imputer = metadata["use_imputer"]

    model = joblib.load(os.path.join(MODEL_DIR, best_model_name))
    feature_columns = joblib.load(os.path.join(MODEL_DIR, "feature_columns.pkl"))
    label_encoder = joblib.load(os.path.join(MODEL_DIR, "label_encoder.pkl"))

    imputer = None
    if use_imputer:
        imputer = joblib.load(os.path.join(MODEL_DIR, "imputer.pkl"))

    print("✅ ML Model Loaded Successfully")

except Exception as e:
    raise RuntimeError(f"❌ Error loading ML model: {e}")


# -----------------------------
# PREDICT FUNCTION
# -----------------------------
def predict_disease(input_dict: dict):
    try:
        # Ensure correct order
        input_data = [input_dict.get(col, 0) for col in feature_columns]

        input_array = np.array(input_data).reshape(1, -1)

        if imputer:
            input_array = imputer.transform(input_array)

        prediction = model.predict(input_array)[0]
        disease = label_encoder.inverse_transform([prediction])[0]

        # Confidence
        confidence = None
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(input_array)
            confidence = float(np.max(probs))

        return {
            "disease": disease,
            "confidence": confidence
        }

    except Exception as e:
        return {"error": str(e)}
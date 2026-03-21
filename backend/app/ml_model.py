import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

model = joblib.load(os.path.join(MODEL_DIR, "best_model.pkl"))
encoder = joblib.load(os.path.join(MODEL_DIR, "label_encoder.pkl"))
feature_columns = joblib.load(os.path.join(MODEL_DIR, "feature_columns.pkl"))


def predict_disease(input_dict: dict):
    # Convert dict → ordered feature list
    features = [input_dict.get(col, 0) for col in feature_columns]

    prediction = model.predict([features])
    return encoder.inverse_transform(prediction)[0]
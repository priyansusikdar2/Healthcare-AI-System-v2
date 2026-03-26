import pandas as pd
import joblib
import os

from sklearn.metrics import accuracy_score, classification_report

# -----------------------------
# PATH SETUP (ROBUST)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "datasets", "processed", "test_cleaned.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")

MODEL_PATH = os.path.join(MODEL_DIR, "best_model.pkl")   # 🔥 use best model
ENCODER_PATH = os.path.join(MODEL_DIR, "label_encoder.pkl")
FEATURE_PATH = os.path.join(MODEL_DIR, "feature_columns.pkl")
IMPUTER_PATH = os.path.join(MODEL_DIR, "imputer.pkl")  # optional (for NN)

# -----------------------------
def evaluate():
    print(f"📥 Loading test dataset from: {DATA_PATH}")
    df = pd.read_csv(r"C:\Users\Priyansu Sikdar\Downloads\health project\backend\app\datasets\processed\test_cleaned.csv")

    print("✅ Dataset Loaded!")
    print("Shape:", df.shape)

    # -----------------------------
    # CLEAN TARGET
    # -----------------------------
    df["prognosis"] = df["prognosis"].astype(str).str.strip()

    X = df.drop("prognosis", axis=1)
    y = df["prognosis"]

    # -----------------------------
    # LOAD ARTIFACTS
    # -----------------------------
    model = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(ENCODER_PATH)
    feature_columns = joblib.load(FEATURE_PATH)

    print("✅ Loaded model, encoder, and feature columns")

    # -----------------------------
    # ALIGN FEATURES (CRITICAL)
    # -----------------------------
    X = X.reindex(columns=feature_columns, fill_value=0)

    # -----------------------------
    # HANDLE IMPUTER (if model needs it)
    # -----------------------------
    if os.path.exists(IMPUTER_PATH):
        try:
            imputer = joblib.load(IMPUTER_PATH)
            X = imputer.transform(X)
            print("🧠 Imputer applied")
        except Exception:
            print("⚠️ Imputer not used (model may be XGBoost)")

    # -----------------------------
    # ENCODE TARGET
    # -----------------------------
    y_encoded = label_encoder.transform(y)

    # -----------------------------
    # PREDICTION
    # -----------------------------
    preds = model.predict(X)

    acc = accuracy_score(y_encoded, preds)

    print(f"\n✅ Accuracy: {acc * 100:.2f}%")

    print("\n📊 Classification Report:")
    print(classification_report(
        y_encoded,
        preds,
        target_names=label_encoder.classes_
    ))

    # -----------------------------
    # OPTIONAL: SHOW SAMPLE OUTPUTS
    # -----------------------------
    decoded_preds = label_encoder.inverse_transform(preds)

    print("\n🔍 Sample Predictions:")
    for i in range(min(5, len(decoded_preds))):
        print(f"Actual: {y.iloc[i]} | Predicted: {decoded_preds[i]}")


# -----------------------------
if __name__ == "__main__":
    evaluate()
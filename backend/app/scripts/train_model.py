import pandas as pd
import joblib
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer

from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier

# -----------------------------
# PATH SETUP (ROBUST)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "datasets", "processed", "train_cleaned.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(MODEL_DIR, exist_ok=True)


# -----------------------------
# TRAIN FUNCTION
# -----------------------------
def train():
    print(f"📥 Loading dataset from: {DATA_PATH}")
    df = pd.read_csv(r"C:\Users\Priyansu Sikdar\Downloads\health project\backend\app\scripts\datasets\processed\train_cleaned.csv")

    print("✅ Dataset Loaded!")
    print("Shape:", df.shape)

    # -----------------------------
    # CLEAN TARGET
    # -----------------------------
    df["prognosis"] = df["prognosis"].astype(str).str.strip()

    # -----------------------------
    # SPLIT FEATURES / TARGET
    # -----------------------------
    X = df.drop("prognosis", axis=1)
    y = df["prognosis"]

    # 🔥 SAVE FEATURE ORDER (VERY IMPORTANT FOR API)
    feature_columns = X.columns.tolist()
    joblib.dump(feature_columns, os.path.join(MODEL_DIR, "feature_columns.pkl"))

    print("📌 Feature count:", len(feature_columns))

    # -----------------------------
    # ENCODE TARGET
    # -----------------------------
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    joblib.dump(label_encoder, os.path.join(MODEL_DIR, "label_encoder.pkl"))

    print("🎯 Classes:", list(label_encoder.classes_))

    # -----------------------------
    # TRAIN / TEST SPLIT
    # -----------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )

    print("\n🚀 Training Models...")

    # =============================
    # ✅ MODEL 1: XGBOOST
    # =============================
    xgb = XGBClassifier(
        n_estimators=150,
        max_depth=6,
        learning_rate=0.1,
        use_label_encoder=False,
        eval_metric='mlogloss'
    )

    xgb.fit(X_train, y_train)

    y_pred_xgb = xgb.predict(X_test)
    xgb_acc = accuracy_score(y_test, y_pred_xgb)

    print(f"✅ XGBoost Accuracy: {xgb_acc:.4f}")

    joblib.dump(xgb, os.path.join(MODEL_DIR, "xgb_model.pkl"))

    # =============================
    # ✅ MODEL 2: NEURAL NETWORK
    # =============================
    imputer = SimpleImputer(strategy="mean")

    X_train_imp = imputer.fit_transform(X_train)
    X_test_imp = imputer.transform(X_test)

    nn = MLPClassifier(hidden_layer_sizes=(128, 64), max_iter=300)

    nn.fit(X_train_imp, y_train)

    y_pred_nn = nn.predict(X_test_imp)
    nn_acc = accuracy_score(y_test, y_pred_nn)

    print(f"✅ Neural Network Accuracy: {nn_acc:.4f}")

    joblib.dump(nn, os.path.join(MODEL_DIR, "nn_model.pkl"))
    joblib.dump(imputer, os.path.join(MODEL_DIR, "imputer.pkl"))

    # -----------------------------
    # 🔥 SELECT BEST MODEL
    # -----------------------------
    if xgb_acc >= nn_acc:
        best_model = xgb
        best_model_name = "xgb_model.pkl"
        print("🏆 Best Model: XGBoost")
    else:
        best_model = nn
        best_model_name = "nn_model.pkl"
        print("🏆 Best Model: Neural Network")

    joblib.dump(best_model, os.path.join(MODEL_DIR, "best_model.pkl"))

    # -----------------------------
    print("\n🎉 Training Complete!")
    print(f"📁 Models saved in: {MODEL_DIR}")


# -----------------------------
if __name__ == "__main__":
    train()
import pandas as pd
import os

# -----------------------------
# PATH CONFIG (FIXED)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, "datasets", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "datasets", "processed")

TRAIN_FILE = os.path.join(RAW_DIR, r"C:\Users\Priyansu Sikdar\Downloads\health project\backend\app\datasets\raw\Training.csv")
TEST_FILE = os.path.join(RAW_DIR, r"C:\Users\Priyansu Sikdar\Downloads\health project\backend\app\datasets\raw\Testing.csv")

os.makedirs(PROCESSED_DIR, exist_ok=True)


# -----------------------------
# PREPROCESS FUNCTION
# -----------------------------
def preprocess(df):
    df = df.copy()

    # 🔹 Remove unwanted column
    if "Unnamed: 133" in df.columns:
        df.drop(columns=["Unnamed: 133"], inplace=True)

    # 🔹 Clean target column
    if "prognosis" in df.columns:
        df["prognosis"] = df["prognosis"].astype(str).str.strip()

    # 🔹 Fill missing values
    df = df.ffill()

    # 🔹 Ensure all feature columns are numeric (VERY IMPORTANT for ML)
    for col in df.columns:
        if col != "prognosis":
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    return df


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def main():
    print("📥 Loading datasets...")

    # FIXED: direct read (no os.path.join mistake)
    train_df = pd.read_csv(TRAIN_FILE)
    test_df = pd.read_csv(TEST_FILE)

    print("🧹 Preprocessing...")

    train_df = preprocess(train_df)
    test_df = preprocess(test_df)

    # 🔥 Ensure SAME columns in train & test
    test_df = test_df.reindex(columns=train_df.columns, fill_value=0)

    # -----------------------------
    # SAVE CLEANED DATA
    # -----------------------------
    train_path = os.path.join(PROCESSED_DIR, "train_cleaned.csv")
    test_path = os.path.join(PROCESSED_DIR, "test_cleaned.csv")

    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)

    print("✅ Preprocessing Complete!")
    print("Train Shape:", train_df.shape)
    print("Test Shape:", test_df.shape)

    print(f"📁 Saved to:\n{train_path}\n{test_path}")


# -----------------------------
if __name__ == "__main__":
    main()
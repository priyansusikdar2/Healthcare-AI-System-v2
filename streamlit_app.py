# streamlit_app.py
import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Healthcare Dashboard", layout="wide")

st.title("🏥 Healthcare Management Dashboard")

menu = st.sidebar.selectbox("Menu", [
    "View Patients",
    "Add Patient",
    "Appointments",
    "Findings",
    "Delivery",
    "Engagement",
    "Literacy",
    "Disease History",
    "ML Prediction"
])

# -------------------------------
# HELPER FUNCTION (SAFE API CALL)
# -------------------------------
def safe_request(method, url, json=None):
    try:
        if method == "GET":
            res = requests.get(url)
        else:
            res = requests.post(url, json=json)

        if res.status_code == 200:
            return res.json()
        else:
            return {"error": f"API Error: {res.status_code}"}

    except Exception as e:
        return {"error": str(e)}


# -------------------------------
# VIEW PATIENTS
# -------------------------------
if menu == "View Patients":
    st.header("👨‍⚕️ Patients List")

    data = safe_request("GET", f"{BASE_URL}/users/patients")

    if "error" in data:
        st.error(data["error"])
    else:
        st.json(data)


# -------------------------------
# ADD PATIENT
# -------------------------------
elif menu == "Add Patient":
    st.header("➕ Add Patient")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    gender = st.selectbox("Gender", ["M", "F", "Other"])

    if st.button("Add Patient"):
        data = safe_request("POST", f"{BASE_URL}/users/", {
            "name": name,
            "age": age,
            "gender": gender
        })

        if "error" in data:
            st.error(data["error"])
        else:
            st.success(data)


# -------------------------------
# APPOINTMENTS
# -------------------------------
elif menu == "Appointments":
    st.header("📅 Appointments")

    if st.button("View Appointments"):
        data = safe_request("GET", f"{BASE_URL}/appointments/")
        st.json(data)

    st.subheader("Create Appointment")
    pid = st.number_input("Patient ID", 1)
    did = st.number_input("Doctor ID", 1)
    date = st.text_input("Date (YYYY-MM-DDTHH:MM:SS)")

    if st.button("Create Appointment"):
        data = safe_request("POST", f"{BASE_URL}/appointments/", {
            "patient_id": pid,
            "doctor_id": did,
            "date": date
        })
        st.success(data)


# -------------------------------
# FINDINGS
# -------------------------------
elif menu == "Findings":
    st.header("🧪 Findings")

    if st.button("View Findings"):
        data = safe_request("GET", f"{BASE_URL}/findings/")
        st.json(data)

    pid = st.number_input("Patient ID")
    finding = st.text_input("Finding")

    if st.button("Add Finding"):
        data = safe_request("POST", f"{BASE_URL}/findings/", {
            "patient_id": pid,
            "finding": finding
        })
        st.success(data)


# -------------------------------
# DELIVERY
# -------------------------------
elif menu == "Delivery":
    st.header("🚑 Healthcare Delivery")

    if st.button("View Delivery"):
        data = safe_request("GET", f"{BASE_URL}/delivery/")
        st.json(data)

    pid = st.number_input("Patient ID")
    service = st.text_input("Service")
    date = st.text_input("Date")

    if st.button("Add Delivery"):
        data = safe_request("POST", f"{BASE_URL}/delivery/", {
            "patient_id": pid,
            "service": service,
            "date": date
        })
        st.success(data)


# -------------------------------
# ENGAGEMENT
# -------------------------------
elif menu == "Engagement":
    st.header("📊 Engagement")

    if st.button("View Engagements"):
        data = safe_request("GET", f"{BASE_URL}/engagements/")
        st.json(data)

    pid = st.number_input("Patient ID")
    activity = st.text_input("Activity")

    if st.button("Add Engagement"):
        data = safe_request("POST", f"{BASE_URL}/engagements/", {
            "patient_id": pid,
            "activity": activity
        })
        st.success(data)


# -------------------------------
# LITERACY
# -------------------------------
elif menu == "Literacy":
    st.header("📚 Health Literacy")

    if st.button("View Records"):
        data = safe_request("GET", f"{BASE_URL}/literacy/")
        st.json(data)

    pid = st.number_input("Patient ID")
    score = st.number_input("Score", 0, 100)

    if st.button("Add Record"):
        data = safe_request("POST", f"{BASE_URL}/literacy/", {
            "patient_id": pid,
            "literacy_score": score
        })
        st.success(data)


# -------------------------------
# DISEASE HISTORY
# -------------------------------
elif menu == "Disease History":
    st.header("🦠 Disease History")

    if st.button("View History"):
        data = safe_request("GET", f"{BASE_URL}/disease_history/")
        st.json(data)

    pid = st.number_input("Patient ID")
    disease = st.text_input("Disease")
    date = st.text_input("Diagnosed On")

    if st.button("Add Record"):
        data = safe_request("POST", f"{BASE_URL}/disease_history/", {
            "patient_id": pid,
            "disease": disease,
            "diagnosed_on": date
        })
        st.success(data)


# -------------------------------
# 🤖 ML PREDICTION (FINAL FIXED)
# -------------------------------
elif menu == "ML Prediction":
    st.header("🤖 Disease Prediction")

    # -----------------------------
    # LOAD SYMPTOMS
    # -----------------------------
    data = safe_request("GET", f"{BASE_URL}/ml/features")

    if "error" in data or "features" not in data:
        st.warning("⚠️ Using fallback symptoms (backend not ready)")

        symptoms = [
            "itching", "skin_rash", "fatigue",
            "vomiting", "headache", "high_fever"
        ]
    else:
        symptoms = data["features"]

    # -----------------------------
    # UI
    # -----------------------------
    selected_symptoms = st.multiselect("Select Symptoms", symptoms)

    input_data = {symptom: 0 for symptom in symptoms}
    for s in selected_symptoms:
        input_data[s] = 1

    # -----------------------------
    # PREDICT
    # -----------------------------
    if st.button("Predict Disease"):
        result = safe_request("POST", f"{BASE_URL}/ml/predict", {
            "data": input_data
        })

        if "error" in result:
            st.error(result["error"])
        elif "disease" in result:
            st.success(f"🧬 Disease: {result['disease']}")

            if result.get("confidence") is not None:
                st.info(f"📊 Confidence: {result['confidence']:.2f}")
        else:
            st.error("Invalid response from API")
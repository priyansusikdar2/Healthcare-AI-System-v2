# streamlit_app.py
import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("🏥 Healthcare Management Dashboard")

menu = st.sidebar.selectbox("Menu", [
    "View Patients",
    "Add Patient",
    "Appointments",
    "Findings",
    "Delivery",
    "Engagement",
    "Literacy",
    "Disease History"
])

# -------------------------------
# VIEW PATIENTS
# -------------------------------
if menu == "View Patients":
    st.header("👨‍⚕️ Patients List")

    res = requests.get(f"{BASE_URL}/users/patients")
    if res.status_code == 200:
        st.json(res.json())
    else:
        st.error("Failed to fetch patients")

# -------------------------------
# ADD PATIENT
# -------------------------------
elif menu == "Add Patient":
    st.header("➕ Add Patient")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    gender = st.selectbox("Gender", ["M", "F", "Other"])

    if st.button("Add Patient"):
        data = {
            "name": name,
            "age": age,
            "gender": gender
        }
        res = requests.post(f"{BASE_URL}/users/", json=data)
        st.success(res.json())

# -------------------------------
# APPOINTMENTS
# -------------------------------
elif menu == "Appointments":
    st.header("📅 Appointments")

    if st.button("View Appointments"):
        res = requests.get(f"{BASE_URL}/appointments/")
        st.json(res.json())

    st.subheader("Create Appointment")
    pid = st.number_input("Patient ID", 1)
    did = st.number_input("Doctor ID", 1)
    date = st.text_input("Date (YYYY-MM-DDTHH:MM:SS)")

    if st.button("Create Appointment"):
        data = {
            "patient_id": pid,
            "doctor_id": did,
            "date": date
        }
        res = requests.post(f"{BASE_URL}/appointments/", json=data)
        st.success(res.json())

# -------------------------------
# FINDINGS
# -------------------------------
elif menu == "Findings":
    st.header("🧪 Findings")

    if st.button("View Findings"):
        res = requests.get(f"{BASE_URL}/findings/")
        st.json(res.json())

    pid = st.number_input("Patient ID")
    finding = st.text_input("Finding")

    if st.button("Add Finding"):
        res = requests.post(f"{BASE_URL}/findings/", json={
            "patient_id": pid,
            "finding": finding
        })
        st.success(res.json())

# -------------------------------
# DELIVERY
# -------------------------------
elif menu == "Delivery":
    st.header("🚑 Healthcare Delivery")

    if st.button("View Delivery"):
        res = requests.get(f"{BASE_URL}/delivery/")
        st.json(res.json())

    pid = st.number_input("Patient ID")
    service = st.text_input("Service")
    date = st.text_input("Date")

    if st.button("Add Delivery"):
        res = requests.post(f"{BASE_URL}/delivery/", json={
            "patient_id": pid,
            "service": service,
            "date": date
        })
        st.success(res.json())

# -------------------------------
# ENGAGEMENT
# -------------------------------
elif menu == "Engagement":
    st.header("📊 Engagement")

    if st.button("View Engagements"):
        res = requests.get(f"{BASE_URL}/engagements/")
        st.json(res.json())

    pid = st.number_input("Patient ID")
    activity = st.text_input("Activity")

    if st.button("Add Engagement"):
        res = requests.post(f"{BASE_URL}/engagements/", json={
            "patient_id": pid,
            "activity": activity
        })
        st.success(res.json())

# -------------------------------
# LITERACY
# -------------------------------
elif menu == "Literacy":
    st.header("📚 Health Literacy")

    if st.button("View Records"):
        res = requests.get(f"{BASE_URL}/literacy/")
        st.json(res.json())

    pid = st.number_input("Patient ID")
    score = st.number_input("Score", 0, 100)

    if st.button("Add Record"):
        res = requests.post(f"{BASE_URL}/literacy/", json={
            "patient_id": pid,
            "literacy_score": score
        })
        st.success(res.json())

# -------------------------------
# DISEASE HISTORY
# -------------------------------
elif menu == "Disease History":
    st.header("🦠 Disease History")

    if st.button("View History"):
        res = requests.get(f"{BASE_URL}/disease_history/")
        st.json(res.json())

    pid = st.number_input("Patient ID")
    disease = st.text_input("Disease")
    date = st.text_input("Diagnosed On")

    if st.button("Add Record"):
        res = requests.post(f"{BASE_URL}/disease_history/", json={
            "patient_id": pid,
            "disease": disease,
            "diagnosed_on": date
        })
        st.success(res.json())
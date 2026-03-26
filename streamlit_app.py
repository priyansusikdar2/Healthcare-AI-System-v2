import streamlit as st
import requests

# -------------------------------
# CONFIG
# -------------------------------
BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Healthcare Dashboard", layout="wide")
st.title("🏥 Healthcare Management Dashboard")

# -------------------------------
# SESSION STATE
# -------------------------------
if "token" not in st.session_state:
    st.session_state.token = None

# -------------------------------
# SAFE API CALL
# -------------------------------
def safe_request(method, url, json=None, form=None):
    try:
        if method == "GET":
            res = requests.get(url)

        elif form:
            res = requests.post(url, data=form)  # for login

        else:
            res = requests.post(url, json=json)

        if res.status_code in [200, 201]:
            return res.json()
        else:
            return {"error": f"{res.status_code}: {res.text}"}

    except Exception as e:
        return {"error": str(e)}

# -------------------------------
# MENU
# -------------------------------
menu = st.sidebar.selectbox("Menu", [
    "Signup",
    "Login",
    "Appointments",
    "Findings",
    "Delivery",
    "Engagement",
    "Literacy",
    "Disease History",
    "ML Prediction"
])

# -------------------------------
# SIGNUP
# -------------------------------
if menu == "Signup":
    st.header("📝 User Signup")

    with st.form("signup_form"):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        name = st.text_input("Full Name")
        age = st.number_input("Age", 0)
        gender = st.selectbox("Gender", ["male", "female", "other"])

        submit = st.form_submit_button("Signup")

    if submit:
        data = safe_request("POST", f"{BASE_URL}/users/", {
            "username": username,
            "email": email,
            "password": password,
            "name": name,
            "age": age,
            "gender": gender
        })

        if "error" in data:
            st.error(data["error"])
        else:
            st.success("✅ Signup successful! Please login.")

# -------------------------------
# LOGIN (FIXED)
# -------------------------------
elif menu == "Login":
    st.header("🔐 User Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        submit = st.form_submit_button("Login")

    if submit:
        data = safe_request(
            "POST",
            f"{BASE_URL}/users/login",
            form={
                "username": username,
                "password": password
            }
        )

        if "error" in data:
            st.error(data["error"])
        else:
            st.session_state.token = data.get("access_token")
            st.success("✅ Login successful!")
            st.write("🔑 Token:", st.session_state.token)

# -------------------------------
# APPOINTMENTS
# -------------------------------
elif menu == "Appointments":
    st.header("📅 Appointments")

    if st.button("View Appointments"):
        data = safe_request("GET", f"{BASE_URL}/appointments/")
        st.json(data)

    with st.form("appointment_form"):
        pid = st.number_input("Patient ID", 1)
        did = st.number_input("Doctor ID", 1)
        date = st.text_input("Date (YYYY-MM-DDTHH:MM:SS)")

        submit = st.form_submit_button("Create Appointment")

    if submit:
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

    with st.form("findings_form"):
        pid = st.number_input("Patient ID", key="f_pid")
        finding = st.text_input("Finding")

        submit = st.form_submit_button("Add Finding")

    if submit:
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

    with st.form("delivery_form"):
        pid = st.number_input("Patient ID", key="d_pid")
        service = st.text_input("Service")
        date = st.text_input("Date (YYYY-MM-DD)")

        submit = st.form_submit_button("Add Delivery")

    if submit:
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

    with st.form("engagement_form"):
        pid = st.number_input("Patient ID", key="e_pid")
        activity = st.text_input("Activity")

        submit = st.form_submit_button("Add Engagement")

    if submit:
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

    with st.form("literacy_form"):
        pid = st.number_input("Patient ID", key="l_pid")
        score = st.number_input("Score", 0, 100)

        submit = st.form_submit_button("Add Record")

    if submit:
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

    with st.form("disease_form"):
        pid = st.number_input("Patient ID", key="dh_pid")
        disease = st.text_input("Disease")
        date = st.text_input("Diagnosed On (YYYY-MM-DD)")

        submit = st.form_submit_button("Add Record")

    if submit:
        data = safe_request("POST", f"{BASE_URL}/disease_history/", {
            "patient_id": pid,
            "disease": disease,
            "diagnosed_on": date
        })
        st.success(data)

# -------------------------------
# ML PREDICTION (FINAL FIXED)
# -------------------------------
elif menu == "ML Prediction":
    st.header("🤖 Disease Prediction")

    data = safe_request("GET", f"{BASE_URL}/ml/features")

    if "error" in data or "features" not in data:
        st.warning("⚠️ Using fallback symptoms")
        symptoms = ["itching", "skin_rash", "fatigue", "vomiting", "headache"]
    else:
        symptoms = data["features"]

    selected_symptoms = st.multiselect("Select Symptoms", symptoms)

    input_data = {s: 0 for s in symptoms}
    for s in selected_symptoms:
        input_data[s] = 1

    if st.button("Predict Disease"):
        result = safe_request("POST", f"{BASE_URL}/ml/predict", {
            "data": input_data
        })

        # 🔍 DEBUG (always visible)
        st.write("🔍 API Response:", result)

        if "error" in result:
            st.error(result["error"])

        elif "disease" in result:
            st.success(f"🧬 Disease: {result['disease']}")
            if result.get("confidence"):
                st.progress(result["confidence"])

        elif "prediction" in result:
            st.success(f"🧬 Disease: {result['prediction']}")

        elif "result" in result:
            st.success(f"🧬 Disease: {result['result']}")

        else:
            st.error("❌ Unexpected API response format")

# 🚑 Healthcare AI System

---

## 📌 Project Overview

This project is a **full-stack AI-powered healthcare system** designed to assist users with disease prediction, healthcare management, and patient engagement. It combines **Machine Learning, FastAPI backend, and a modern frontend** to deliver real-world healthcare insights with an industry-ready architecture.

---

## 🚀 Key Features

### 🧠 AI-Based Disease Prediction

* Predict diseases based on user-selected symptoms
* Uses trained ML models (**XGBoost + Neural Networks**)
* Supports **132-feature vector input (high accuracy)**
* Returns **confidence score + prediction result**
* Handles **dynamic symptom selection (multi-select UI)**

---

### ⚙️ FastAPI Backend (Production-Ready)

* RESTful API architecture
* Modular router-based structure
* Scalable and clean code design
* Integrated ML prediction pipeline (`/ml/predict`)
* Built-in API testing with Swagger UI

---

### 🎨 Advanced Frontend (Modern UI)

* Built with **HTML, CSS, JavaScript**
* ✨ Glassmorphism + Glow UI effects
* 📊 Interactive Dashboard with charts
* 🌙 Dark / Light mode toggle
* 🌐 Multilingual support (English + Hindi)
* 📱 Fully responsive design

---

### 📊 Smart Dashboard Features

* 📈 Activity charts (Predictions & Patients)
* 🧠 AI Health Insights section
* 📁 Patient records management (frontend + backend hybrid)
* 🧾 Real-time data visualization

---

### 🗄️ Database Integration

* SQLite (`healthcare.db`)
* Stores:

  * Users
  * Patients
  * Appointments
  * Findings
  * Engagement records
  * Disease history

---

### 📡 Streamlit ML Interface

* Interactive ML testing dashboard
* Real-time predictions
* Model experimentation UI

---

# 📡 API Endpoints

---

## 🔹 GET Requests

| Name                | Method | URL                 |
| ------------------- | ------ | ------------------- |
| Login (User)        | POST   | `/users/login`      |
| API Health Check    | GET    | `/`                 |
| Ping                | GET    | `/ping`             |
| Get Findings        | GET    | `/findings/`        |
| Get Deliveries      | GET    | `/delivery/`        |
| Get Engagements     | GET    | `/engagements/`     |
| Get Health Literacy | GET    | `/literacy/`        |
| Get Disease History | GET    | `/disease_history/` |
| Get Appointments    | GET    | `/appointments/`    |
| Get ML Features     | GET    | `/ml/features`      |

---

## 🔹 POST Requests

| Name                | Method | URL                 | JSON Body Example                                                                                       |
| ------------------- | ------ | ------------------- | ------------------------------------------------------------------------------------------------------- |
| Signup (User)       | POST   | `/users/`           | `{"username":"test","email":"test@gmail.com","password":"1234","name":"Test","age":22,"gender":"male"}` |
| Create Appointment  | POST   | `/appointments/`    | `{"patient_id":1,"doctor_id":2,"date":"2026-03-22T10:30:00"}`                                           |
| Add Finding         | POST   | `/findings/`        | `{"patient_id":1,"finding":"High BP"}`                                                                  |
| Add Delivery Record | POST   | `/delivery/`        | `{"patient_id":1,"service":"Medication","date":"2026-03-22"}`                                           |
| Add Engagement      | POST   | `/engagements/`     | `{"patient_id":1,"activity":"Workshop"}`                                                                |
| Add Literacy Record | POST   | `/literacy/`        | `{"patient_id":1,"literacy_score":85}`                                                                  |
| Add Disease History | POST   | `/disease_history/` | `{"patient_id":1,"disease":"Diabetes"}`                                                                 |
| 🤖 ML Prediction    | POST   | `/ml/predict`       | `{"data":{"itching":1,"skin_rash":1,"fatigue":1}}`                                                      |

---

## 🔹 Sample ML Response

```json
{
  "prediction": "Fungal infection",
  "confidence": 0.95
}
```

---

## 🧠 Machine Learning Workflow

1. Data Cleaning
2. Feature Engineering
3. Model Training (`train_model.py`)
4. Model Evaluation
5. Deployment via FastAPI

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, Python
* **Frontend:** HTML, CSS, JavaScript
* **ML:** Scikit-learn, Pandas, NumPy, XGBoost
* **Database:** SQLite
* **Visualization:** Chart.js, Streamlit

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/healthcare-ai-system.git
cd healthcare-ai-system
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Backend

```bash
uvicorn backend.app.main:app --reload
```

👉 http://127.0.0.1:8000
👉 http://127.0.0.1:8000/docs
👉 thunderclient (vs code)

---

### 5️⃣ Run Frontend

* Open `frontend/index.html`
* OR use Live Server
* http://localhost:5500

---

### 6️⃣ Run Streamlit

```bash
streamlit run streamlit_app.py
```

---

## 📁 Important Files

* `main.py` → FastAPI entry
* `ml_model.py` → ML logic
* `train_model.py` → Training pipeline
* `streamlit_app.py` → ML UI
* `predict.js` → Frontend ML integration

---

## 🌟 Major Enhancements

* ✅ Full ML Integration with FastAPI (`/ml/predict`)
* ✅ Dynamic Symptom → Feature Vector Conversion
* ✅ Advanced Dashboard with Charts (Chart.js)
* ✅ AI Insights & Prediction History
* ✅ Multilingual Support (EN + HI)
* ✅ Dark / Light Mode Toggle
* ✅ Glassmorphism UI (modern design)
* ✅ LocalStorage-based frontend persistence
* ✅ Robust API Error Handling
* ✅ Fully Debugged Frontend-Backend Integration

---

## 🚀 Future Enhancements

* 🔐 JWT Role-Based Authentication (Doctor / Patient)
* 📊 Advanced Analytics Dashboard
* 🧠 Explainable AI (Why this prediction?)
* 🏥 Doctor Recommendation System
* 📄 PDF Report Generation
* ☁️ Deployment (AWS / Render / Docker)
* 📱 Mobile App (React Native / Flutter)

---

## ⚠️ Notes

Avoid committing:

* `__pycache__/`
* `.db`
* `.env`
* `.pkl` (use Git LFS)

---

## 👨‍💻 Author

**Priyansu Sikdar**

---

## 📜 License

MIT License

---

## 🔥 Final Note

This project demonstrates:

* ✅ Full-stack development
* ✅ AI + ML integration
* ✅ Scalable backend architecture
* ✅ Real-world healthcare application design

👉 Perfect for **Resume • Portfolio • Hackathons • Production-ready systems**

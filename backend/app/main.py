# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# -----------------------------
# DATABASE
# -----------------------------
from app.database import Base, engine

# 🔥 IMPORTANT: Import all models so tables register
import app.models


# -----------------------------
# ROUTERS
# -----------------------------
from app.routers import (
    user_router,
    appointment_router,
    findings_router,
    engagement_router,
    disease_router,
    delivery_router,
    literacy_router,
    ml_router
)


# -----------------------------
# FASTAPI APP INIT
# -----------------------------
app = FastAPI(
    title="🏥 Healthcare Management API",
    description="Industry-level Healthcare Backend using FastAPI + SQLAlchemy + ML Integration",
    version="1.2.0"
)


# -----------------------------
# STARTUP EVENT (BETTER PRACTICE)
# -----------------------------
@app.on_event("startup")
def startup_event():
    print("🚀 Starting Healthcare API...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables ready")


# -----------------------------
# CORS CONFIG
# -----------------------------
origins = ["*"]  # ⚠️ Restrict in production

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# ROUTES
# -----------------------------
app.include_router(user_router.router, prefix="/users", tags=["Users"])
app.include_router(appointment_router.router, prefix="/appointments", tags=["Appointments"])
app.include_router(findings_router.router, prefix="/findings", tags=["Findings"])
app.include_router(delivery_router.router, prefix="/delivery", tags=["Healthcare Delivery"])
app.include_router(engagement_router.router, prefix="/engagements", tags=["Engagements"])
app.include_router(literacy_router.router, prefix="/literacy", tags=["Health Literacy"])
app.include_router(disease_router.router, prefix="/disease_history", tags=["Disease History"])

# 🔥 ML ROUTES
app.include_router(
    ml_router.router,
    prefix="/ml",
    tags=["ML Predictions"]
)


# -----------------------------
# HEALTH CHECK
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "🚀 Healthcare Management API is running!",
        "docs": "/docs"
    }


@app.get("/ping")
def ping():
    return {"msg": "pong"}


# -----------------------------
# OPTIONAL: DEBUG ROUTE
# -----------------------------
@app.get("/debug/routes")
def list_routes():
    return [{"path": route.path, "name": route.name} for route in app.routes]
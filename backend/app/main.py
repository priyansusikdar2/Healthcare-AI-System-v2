# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Database
from .database import Base, engine

# 🔥 IMPORTANT: Import all models so tables are registered
import app.models

# Routers
from .routers import (
    user_router,
    appointment_router,
    findings_router,
    engagement_router,
    disease_router,
    delivery_router,
    literacy_router 
)

# -----------------------------
# CREATE DATABASE TABLES
# -----------------------------
Base.metadata.create_all(bind=engine)

# -----------------------------
# FASTAPI APP INIT
# -----------------------------
app = FastAPI(
    title="Healthcare Management API",
    description="Industry-level Healthcare Backend using FastAPI + SQLAlchemy",
    version="1.1.0"
)

# -----------------------------
# CORS CONFIG
# -----------------------------
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Change in production
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

# -----------------------------
# HEALTH CHECK
# -----------------------------
@app.get("/")
def root():
    return {"message": "🚀 Healthcare Management API is running!"}


@app.get("/ping")
def ping():
    return {"msg": "pong"}
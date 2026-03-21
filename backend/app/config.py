import os

# You can use environment variables or hardcode your database URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./healthcare.db")

# Optional: SQLAlchemy settings
SQLALCHEMY_ECHO = True  # Logs all SQL queries, useful for debugging
SQLALCHEMY_TRACK_MODIFICATIONS = False
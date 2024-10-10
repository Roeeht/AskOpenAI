import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Prevents SQLAlchemy from emitting unnecessary signals
    FLASK_PORT = os.environ.get("FLASK_PORT", 5000)  # Default to 5000 if not set
    DB_PORT = os.environ.get("DB_PORT", 5432) # Default to 5432 if not set


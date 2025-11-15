from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8080))
    DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1"]
    DATA_FOLDER = os.getenv("DATA_FOLDER", "data")
    ALLOWED_FIELDS = [f.strip() for f in os.getenv("ALLOWED_FIELDS", "").split(',')]

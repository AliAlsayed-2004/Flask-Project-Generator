import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.join(BASE_DIR, 'app', 'database')
os.makedirs(DB_DIR, exist_ok=True)

DB_PATH = os.path.join(DB_DIR, 'default.db')

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'
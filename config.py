import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secretkey")
    
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:123@localhost:5432/flight_db"
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret")
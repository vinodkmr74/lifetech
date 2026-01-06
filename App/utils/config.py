import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60)
)

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in .env")


CORS_ORIGINS = os.getenv("CORS_ORIGINS", "")
# convert string → list
ALLOWED_ORIGINS = [origin.strip() for origin in CORS_ORIGINS.split(",") if origin]
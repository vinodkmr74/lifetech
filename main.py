from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from App.database import Base, engine
from App.routers import singin, login, token, authorization
from App.utils.config import ALLOWED_ORIGINS


app = FastAPI()

# Base.metadata.create_all(bind=engine)
# SAFE: DB init at startup (NOT import time)
@app.on_event("startup")
def startup_event():
    try:
        Base.metadata.create_all(bind=engine)
        print(" Database connected & tables created")
    except Exception as e:
        print("Database connection failed:", e)


app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(singin.router)
app.include_router(login.router)
app.include_router(token.router)
app.include_router(authorization.router)

@app.get("/")
def home():
    return {"message": "FastAPI running successfully"}

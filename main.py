from fastapi import FastAPI
from App.database import Base, engine
from App.routers import singin

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(singin.router,tags=["singin"])

@app.get("/")
def home():
    return {"message": "FastAPI running successfully"}

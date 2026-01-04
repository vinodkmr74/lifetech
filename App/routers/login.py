from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from App.database import SessionLocal
from App.models.model import Singin
from App.utils.security import verify_password

router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(Singin).filter(Singin.email == email).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {
        "message": "Login successful",
        "user": {
            "id": user.id,
            "email": user.email
        }
    }

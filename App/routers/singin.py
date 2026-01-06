from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from App.database import SessionLocal
from App.models.model import Singin
from App.utils.security import hash_password

router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signin")
def signin(
    email: str = Form(...),
    password: str = Form(...),
    role: str = Form("user"),   # 👈 ADD ROLE
    db: Session = Depends(get_db)
):
    user = Singin(
        email=email,
        password=hash_password(password),
        role=role
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "User registered successfully",
        "user": {
            "id": user.id,
            "email": user.email,
            "role": user.role
        }
    }

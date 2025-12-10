# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from App.database import SessionLocal
# from App.models.model import Singin  # your SQLAlchemy model

# # router = APIRouter()
# router = APIRouter(prefix="/api")  # ✅ important: /api prefix


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @router.post("/singin")  # you can rename to /signin if you want
# def singin(email: str, password: str, db: Session = Depends(get_db)):
#     # ✅ Create a new Singin object (NOT login)
#     new_user = Singin(email=email, password=password)

#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     # ✅ Return proper fields (don't mix name/email, etc.)
#     return {
#         "message": "User added successfully",
#         "login": {
#             "id": new_user.id,
#             "email": new_user.email,
#             "password": new_user.password,  # in real apps don’t return plain password
#         },
#     }




from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from App.database import SessionLocal
from App.models.model import Singin

router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- SIGNUP ----------------
@router.post("/singin")   # register
def singin(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    new_user = Singin(email=email, password=password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User added successfully",
        "login": {
            "id": new_user.id,
            "email": new_user.email,
        },
    }


# ---------------- LOGIN ----------------
@router.post("/login")
def login(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = (
        db.query(Singin)
        .filter(Singin.email == email, Singin.password == password)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "message": "Login successful",
        "user": {
            "id": user.id,
            "email": user.email,
        }
    }

# from fastapi import APIRouter, Depends, Form
# from sqlalchemy.orm import Session
# from App.database import SessionLocal
# from App.models.model import Singin
# from App.utils.security import hash_password

# router = APIRouter(prefix="/api")

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/signin")
# def signin(
#     email: str = Form(...),
#     password: str = Form(...),
#     role: str = Form("user"),   # 👈 ADD ROLE
#     db: Session = Depends(get_db)
# ):
    
#     user = Singin(
#         email=email,
#         password=hash_password(password),
#         role=role
#     )
#     db.add(user)
#     db.commit()
#     db.refresh(user)

#     return {
#         "message": "User registered successfully",
#         "user": {
#             "id": user.id,
#             "email": user.email,
#             "role": user.role
#         }
#     }


from fastapi import APIRouter, Depends, Form, HTTPException
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
    role: str = Form("user"),
    db: Session = Depends(get_db)
):
    if len(password) < 6:
        raise HTTPException(status_code=400, detail="Password too short")

    if len(password.encode("utf-8")) > 72:
        raise HTTPException(
            status_code=400,
            detail="Password must be max 72 characters"
        )

    existing_user = db.query(Singin).filter(Singin.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

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

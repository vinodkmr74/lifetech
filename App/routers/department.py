from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from App.database import SessionLocal
from App.models.department import DepartmentImage
from fastapi import Request

from App.models.docter_image import DoctorImage

router = APIRouter(prefix="/api",tags=["Department"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/department/create")
def create_department(
    image_path: str = Form(...),
    department_name: str = Form(...),
    detail: str = Form(...),
    db: Session = Depends(get_db)
):
    department = DepartmentImage(
        image_path=image_path,
        department_name=department_name,
        detail=detail
    )
    db.add(department)
    db.commit()
    db.refresh(department)

    return {
        "message": "Department created",
        "id": department.id
    }


@router.get("/department/all")
def get_all_departments(request: Request, db: Session = Depends(get_db)):
    base_url = str(request.base_url)
    departments = db.query(DepartmentImage).all()

    return {
        "status": True,
        "data": [
            {
                "id": d.id,
                "department_name": d.department_name,
                # "image_path": d.image_path,
                "image_url": f"{base_url}images/{d.image_path}",

                "detail": d.detail,
                "doctor_images": [
                    {
                        "doctor_name": doc.doctor_name,
                        # "image_path": doc.image_path
                        "dr_image_url": f"{base_url}images/{doc.image_path}"
                    }
                    for doc in d.doctor_images
                ]
            }
            for d in departments
        ]
    }
    
@router.get("/department/{department_id}")
def get_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    department = db.query(DepartmentImage).filter(
        DepartmentImage.id == department_id
    ).first()

    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    return {
        "status": True,
        "id": department.id,
        "department_name": department.department_name,
        "image_path": department.image_path,
        "detail": department.detail,
        "doctor_images": [
            {
                "doctor_name": doctor.doctor_name,
                "image_path": doctor.image_path
            }
            for doctor in department.doctor_images
        ]
    }

@router.post("/department/{department_id}/doctor-image")
def add_doctor_image(
    department_id: int,
    image_path: str = Form(...),
    doctor_name: str = Form(...),
    db: Session = Depends(get_db)
):
    department = db.query(DepartmentImage).filter(
        DepartmentImage.id == department_id
    ).first()

    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    image = DoctorImage(
        image_path=image_path,
        doctor_name=doctor_name,
        department_id=department_id
    )

    db.add(image)
    db.commit()

    return {"message": "Doctor image added"}


@router.put("/department/update/{department_id}")
def update_department(
    department_id: int,
    image_path: str = Form(None),
    department_name: str = Form(None),
    detail: str = Form(None),
    db: Session = Depends(get_db)
):
    department = db.query(DepartmentImage).filter(
        DepartmentImage.id == department_id
    ).first()

    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    if image_path:
        department.image_path = image_path
    if department_name:
        department.department_name = department_name
    if detail:
        department.detail = detail

    db.commit()
    return {"message": "Department updated"}


@router.delete("/doctor-image/delete/{image_id}")
def delete_doctor_image(
    image_id: int,
    db: Session = Depends(get_db)
):
    image = db.query(DoctorImage).filter(
        DoctorImage.id == image_id
    ).first()

    if not image:
        raise HTTPException(status_code=404, detail="Doctor image not found")

    db.delete(image)
    db.commit()

    return {"message": "Doctor image deleted"}


@router.delete("/department/delete/{department_id}")
def delete_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    department = db.query(DepartmentImage).filter(
        DepartmentImage.id == department_id
    ).first()

    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    db.delete(department)
    db.commit()

    return {"message": "Department deleted"}


@router.put("/doctor-image/update/{doctor_id}")
def update_doctor_image(
    doctor_id: int,
    doctor_name: str = Form(None),
    image_path: str = Form(None),
    db: Session = Depends(get_db)
):
    doctor = db.query(DoctorImage).filter(
        DoctorImage.id == doctor_id
    ).first()

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    if doctor_name:
        doctor.doctor_name = doctor_name

    if image_path:
        doctor.image_path = image_path

    db.commit()

    return {
        "status": True,
        "message": "Doctor image updated successfully",
        "data": {
            "id": doctor.id,
            "doctor_name": doctor.doctor_name,
            "image_path": doctor.image_path
        }
    }

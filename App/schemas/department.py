from pydantic import BaseModel
from typing import List

class DoctorImageCreate(BaseModel):
    image_path: str
    doctor_name: str


class DoctorImageResponse(DoctorImageCreate):
    id: int

    class Config:
        from_attributes = True


class DepartmentCreate(BaseModel):
    image_path: str
    department_name: str
    detail: str


class DepartmentUpdate(BaseModel):
    image_path: str | None = None
    department_name: str | None = None
    detail: str | None = None


class DepartmentResponse(DepartmentCreate):
    id: int
    doctor_images: List[DoctorImageResponse] = []

    class Config:
        from_attributes = True

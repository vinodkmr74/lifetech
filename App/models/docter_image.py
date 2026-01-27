from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from App.database import Base

class DoctorImage(Base):
    __tablename__ = "doctor_images"

    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String(225), nullable=False)
    doctor_name = Column(String(225), nullable=False)

    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship(
        "DepartmentImage",      
        back_populates="doctor_images"
    )

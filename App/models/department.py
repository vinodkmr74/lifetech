from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from App.database import Base

class DepartmentImage(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String(225), nullable=False)
    department_name = Column(String(225), nullable=False)
    detail = Column(Text, nullable=False)

    doctor_images = relationship(
        "DoctorImage",  
        back_populates="department",
        cascade="all, delete"
    )


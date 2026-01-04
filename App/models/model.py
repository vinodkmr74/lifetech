from sqlalchemy import Column, Integer, String
from App.database import Base

class Singin(Base):
    __tablename__ = "singin"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    role = Column(String(30), default="user")

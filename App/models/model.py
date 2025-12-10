from sqlalchemy import Column, Integer, String
from App.database import Base

class Singin(Base):   # you can rename to Signin if you want
    __tablename__ = "login"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))

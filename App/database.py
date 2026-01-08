from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from decouple import config
from dotenv import load_dotenv
import os
import pymysql



pymysql.install_as_MySQLdb()
load_dotenv() 

# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(DATABASE_URL, pool_pre_ping=True,pool_recycle=280)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


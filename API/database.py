from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"postgresql+psycopg2://{os.getenv("DB_PATH")}"

engine = create_engine(DATABASE_URL)

session_local =  sessionmaker(bind = engine, autocommit = False)

class Base(DeclarativeBase):
    pass

def getdb():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
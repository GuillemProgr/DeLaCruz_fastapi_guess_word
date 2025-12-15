from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Field, Session, create_engine,select
from dotenv import load_dotenv
from typing import List
import os

app = FastAPI()
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
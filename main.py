from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv
from models.abecedari import Abecedari
from models.paraula import Paraula
from services.service_paraula import obtenir_paraula_aleatoria
from services.service_abecedari import obtenir_abecedari
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

#Segon endpoint retornem una llista amb les lletres segon
@app.get("/paraula/abecedari/{idioma}", response_model=dict)
def get_abecedari(idioma: str, db: Session = Depends(get_db)):
    return obtenir_abecedari(idioma, db)

#Primer endpoint generem una paraula random segons l'idioma
@app.get("/paraula/{idioma}", response_model=dict)
def get_paraula(idioma: str, db: Session = Depends(get_db)):
    return obtenir_paraula_aleatoria(idioma, db)
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv
from models.abecedari import Abecedari, AbecedariResponse
from models.paraula import Paraula, ParaulaResponse
from models.instruccions import Instruccions, InstruccionsResponse
from services.service_paraula import obtenir_paraula_aleatoria
from services.service_abecedari import obtenir_abecedari
from services.service_instruccions import obtenir_instruccions
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
@app.get("/paraula/abecedari/{idioma}", response_model=AbecedariResponse)
def get_abecedari(idioma: str, db: Session = Depends(get_db)):
    result = obtenir_abecedari(idioma, db)
    return result

#Primer endpoint generem una paraula random segons l'idioma
@app.get("/llista/{idioma}", response_model=ParaulaResponse)
def get_paraula(idioma: str, db: Session = Depends(get_db)):
    result = obtenir_paraula_aleatoria(idioma, db)
    return result

#Tercer endpoint retornem les instruccions del joc segons l'idioma
@app.get("/instruccions/{idioma}", response_model=InstruccionsResponse)
def get_instruccions(idioma: str, db: Session = Depends(get_db)):
    result =  obtenir_instruccions(idioma, db)
    return result
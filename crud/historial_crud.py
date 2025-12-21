from sqlmodel import Session, select
from models.historial import Historial,HistorialResponse

def get_historial_actiu(db: Session, usuari: str):
    #Consultem si hi ha una partida activa de algun usuari
    stmt = select(Historial).where(
        Historial.usuari == usuari,
        Historial.finalitza == False
    )
    return db.exec(stmt).first()

def guardar_historial(db: Session, historial:Historial):
    #Desem un nou registre d'historial a la base de dades
    db.add(historial)
    db.commit()
    db.refresh(historial)
    return historial

def get_historial_per_usuari(db: Session, usuari: str):
    #Obtenim tots el registres d'historial segons l'usuari
    stmt = select(Historial).where(Historial.usuari == usuari)
    return db.exec(stmt).all()

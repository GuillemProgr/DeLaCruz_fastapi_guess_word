from sqlmodel import Session, select
from models.paraula import Paraula

def get_diccionario(db: Session, idioma: str):
    stmt = select(Paraula).where(Paraula.idioma == idioma)
    return db.exec(stmt).all()

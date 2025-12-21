from sqlmodel import Session, select
from models.instruccions import Instruccions

#Fem la consulta a la bd per obtenir la paraula d'un idioma concret
def get_instruccions(db: Session, idioma: str):
    stmt = select(Instruccions).where(Instruccions.idioma == idioma)
    return db.exec(stmt).first()

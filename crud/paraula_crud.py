from sqlmodel import Session, select
from models.paraula import Paraula

#Fem la consulta a la bd per obtenir la paraula d'un idioma concret
def get_paraules_per_idioma(db: Session, idioma: str):
    stmt = select(Paraula).where(Paraula.idioma == idioma)
    return db.exec(stmt).all()

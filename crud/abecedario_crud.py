from sqlmodel import Session, select
from models.abecedari import Abecedari

#Fem la consulta a la bd per obtenir l'abecedari d'un idioma concret
def get_abecedario(db: Session, idioma: str):
    stmt = select(Abecedari).where(Abecedari.idioma == idioma)
    return db.exec(stmt).all()

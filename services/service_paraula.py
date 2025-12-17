from fastapi import HTTPException
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError
from random import choice
from crud.paraula_crud import get_paraules_per_idioma

def obtenir_paraula_aleatoria(idioma: str, db: Session):
    try:
        #Validem l'idioma
        if idioma not in ["ca", "es", "en"]:
            raise HTTPException(status_code=400, detail="Idioma invàlid")

        paraules = get_paraules_per_idioma(db, idioma)

        if not paraules:
            raise HTTPException(status_code=404, detail="No hi ha paraula disponible")
        #Generem la paraula random
        paraula = choice(paraules)

        return {
            "paraula": paraula.paraula,
        }

    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity error en consulta a BD")
    except Exception:
        raise HTTPException(status_code=500, detail="Error intern del servidor")


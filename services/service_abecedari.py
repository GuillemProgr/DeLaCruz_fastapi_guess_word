from fastapi import HTTPException
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError
from models.abecedari import AbecedariResponse
from crud.abecedario_crud import get_abecedario

IDIOMES_SUPORTATS = ["ca", "es", "en"]

def obtenir_abecedari(idioma: str, db: Session):
    try:
        #Validem l'idioma
        if idioma not in IDIOMES_SUPORTATS:
            raise HTTPException(status_code=400, detail="Idioma no suportat")

        registres = get_abecedario(db, idioma)

        if not registres:
            raise HTTPException(status_code=404, detail="Error en l’alfabet")

        # S’agafa el primer registre
        registre = registres[0]

        # Convertim la cadena de lletres en una llista
        lletres = registre.lletres.split(",")

        if not lletres:
            raise ValueError

        return AbecedariResponse(
            idioma=idioma,
            lletres=lletres
        )

    except ValueError:
        raise HTTPException(status_code=422, detail="Dades incorrectes")
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity error en consulta a BD")
    except Exception:
        raise HTTPException(status_code=500, detail="Error intern del servidor")

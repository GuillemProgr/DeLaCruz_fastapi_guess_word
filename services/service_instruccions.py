from fastapi import HTTPException
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError, MultipleResultsFound
from models.instruccions import InstruccionsResponse
from crud.instruccions_crud import get_instruccions

IDIOMES_SUPORTATS = ["ca", "es", "en"]

def obtenir_instruccions(idioma: str, db: Session):
    try:
        # Idioma no suportat
        if idioma not in IDIOMES_SUPORTATS:
            raise HTTPException(
                status_code=404,
                detail="Idioma no disponible"
            )

        instruccio = get_instruccions(db, idioma)

        # No hi ha instruccions per l’idioma
        if not instruccio:
            raise HTTPException(
                status_code=404,
                detail="Idioma no disponible"
            )
        return InstruccionsResponse(
            idioma=instruccio.idioma,
            instruccions=instruccio.instruccions
        )

    except MultipleResultsFound:
        raise HTTPException(
            status_code=409,
            detail="MultipleResultsFound"
        )

    except KeyError:
        raise HTTPException(
            status_code=422,
            detail="KeyError"
        )

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Integrity error en consulta a BD"
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Error intern del servidor"
        )

from fastapi import HTTPException
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError
from models.historial import Historial, HistorialResponse, HistorialRequest
from crud.historial_crud import guardar_historial, get_historial_actiu, get_historial_per_usuari

def guardar_partida(request: HistorialRequest, db: Session):
    try:
        activa = get_historial_actiu(db, request.usuari)
        if activa and not request.finalitza:
            raise HTTPException(status_code=409, detail="Conflicte en guardar partida activa")
        # Crem l’objecte Historial amb les dades rebudes del client
        historial = Historial(
            usuari=request.usuari,
            partides_jugades=request.partides_jugades,
            partides_guanyades=request.partides_guanyades,
            puntuacio_actual=request.puntuacio_actual,
            finalitza=request.finalitza,
            data=request.data
        )

        guardar_historial(db, historial)
        #Retornem la resposta amb el model de sortida
        return HistorialResponse(
            usuari=historial.usuari,
            partides_jugades=historial.partides_jugades,
            partides_guanyades=historial.partides_guanyades,
            puntuacio_actual=historial.puntuacio_actual,
            finalitza=historial.finalitza,
            data=historial.data
        )

    except IntegrityError:
        raise HTTPException(status_code=422, detail="Error en el JSON de l’historial")

    except Exception:
        raise HTTPException(status_code=500, detail="Error intern del servidor")


def obtenir_historial(usuari: str, db: Session):
    try:
        historial = get_historial_per_usuari(db, usuari)

        if not historial:
            raise HTTPException(status_code=404, detail="No hi ha historial disponible")

        return [
            HistorialResponse(
                usuari=h.usuari,
                partides_jugades=h.partides_jugades,
                partides_guanyades=h.partides_guanyades,
                puntuacio_actual=h.puntuacio_actual,
                finalitza=h.finalitza,
                data=h.data
            )
            for h in historial
        ]

    except Exception:
        raise HTTPException(status_code=500, detail="Error intern del servidor")

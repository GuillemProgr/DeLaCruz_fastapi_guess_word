from sqlmodel import SQLModel, Field
from datetime import datetime

class Historial(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    usuari: str
    partides_jugades: int
    partides_guanyades: int
    puntuacio_actual: int
    finalitza: bool
    data: datetime


class HistorialResponse(SQLModel):
    usuari: str
    partides_jugades: int
    partides_guanyades: int
    puntuacio_actual: int
    finalitza: bool
    data: datetime


class HistorialRequest(SQLModel):
    usuari: str
    partides_jugades: int
    partides_guanyades: int
    puntuacio_actual: int
    finalitza: bool
    data: datetime

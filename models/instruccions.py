from sqlmodel import SQLModel,Field

#Creem la taula instruccions
class Instruccions(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    idioma: str
    instruccions: str

class InstruccionsResponse(SQLModel):
    idioma: str
    instruccions: str
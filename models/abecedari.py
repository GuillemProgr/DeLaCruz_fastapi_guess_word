from sqlmodel import SQLModel, Field

class Abecedari(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    idioma: str
    lletres: str

class AbecedariResponse(SQLModel):
    idioma: str
    lletres: list[str]

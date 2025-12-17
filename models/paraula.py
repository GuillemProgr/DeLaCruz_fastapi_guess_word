from sqlmodel import SQLModel,Field

class Paraula(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    paraula: str
    idioma: str

class ParaulaResponse(SQLModel):
    paraula: str
    idioma: str
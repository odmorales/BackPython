import datetime as _dt
import pydantic as _pydantic

class _BasePerson(_pydantic.BaseModel):
    identificacion: str
    nombre: str
    apellido: str
    edad: int
    genero: str
    
class Person(_BasePerson):
    id: int
    pulsaciones: float

    class Config:
        orm_mode = True
    

class CreatePerson(_BasePerson):
    pass
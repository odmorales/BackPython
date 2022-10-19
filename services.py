from json.encoder import INFINITY
from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_person(db: "Session", person_id: int):
    return db.query(_models.Person).filter(_models.Person.identificacion == person_id).first()

def get_persons(db: "Session", skip: int = 0, limit: int = 100):
    return db.query(_models.Person).offset(skip).limit(limit).all()

def create_person(person: schemas.CreatePerson ,db: "Session"):

    db_person = _models.Person(nombre=person.nombre, apellido = person.apellido,
                               identificacion = person.identificacion, edad = person.edad,
                               genero = person.genero, pulsaciones = calcular_pulsaciones(person.edad, person.genero))
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    
    return db_person

def calcular_pulsaciones(edad: int, genero: str) -> float: 
    if genero.upper() == "M":
        return (210 - edad) / 10
    elif genero.upper() == "F":
        return (220 - edad) / 10
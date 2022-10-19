import datetime as _dt
import sqlalchemy as _sql
import database as _database

class Person(_database.Base):
    __tablename__ = "persons"
    
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nombre = _sql.Column(_sql.String)
    apellido = _sql.Column(_sql.String)
    identificacion =  _sql.Column(_sql.String)
    edad = _sql.Column(_sql.Integer)
    genero = _sql.Column(_sql.String)
    pulsaciones = _sql.Column(_sql.Float)

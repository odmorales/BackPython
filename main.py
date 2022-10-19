from typing import TYPE_CHECKING,List
import fastapi as _fastapi
import schemas as schemas
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

import sqlalchemy.orm as _orm
import services as services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/persona/", response_model=schemas.Person)
def guardar_persona(person: schemas.CreatePerson, db:_orm.Session = _fastapi.Depends(services.get_db)):
    
    return services.create_person(db=db, person=person)

@app.get("/api/persons/", response_model=List[schemas.Person])
def get_persons(db:_orm.Session =_fastapi.Depends(services.get_db)):
    return services.get_persons(db=db)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
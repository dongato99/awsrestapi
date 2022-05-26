from fastapi import APIRouter, HTTPException
from config.db import conn
from models.profesor import profesores
from schemas.profesor import Profesor


profesor = APIRouter()




@profesor.get("/profesores")
def get_profesores():
    return conn.execute(profesores.select()).fetchall()


@profesor.post('/profesores', status_code=201)
def create_profesor(profesor: Profesor):
    new_profesor = {"numeroEmpleado": profesor.numeroEmpleado, "nombres": profesor.nombres,
                  "apellidos": profesor.apellidos, "horasClase": profesor.horasClase}
    result = conn.execute(profesores.insert().values(new_profesor))
    return conn.execute(profesores.select().where(profesores.c.id == result.lastrowid)).first()


@profesor.get('/profesores/{id}')
def get_profesor(id: str):
    if conn.execute(profesores.select().where(profesores.c.id == id)).first() is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return conn.execute(profesores.select().where(profesores.c.id == id)).first()


@profesor.delete('/profesores/{id}')
def delete_profesor(id: str):
    if conn.execute(profesores.select().where(profesores.c.id == id)).first() is None:
        raise HTTPException(status_code=404, detail="Item not found")

    conn.execute(profesores.delete().where(profesores.c.id == id)) 
    return {"message": "Profesor eliminado"}


@profesor.put('/profesores/{id}')
def editar_profesor(id: str, profesor: Profesor):
    conn.execute(profesores.update().values(numeroEmpleado=profesor.numeroEmpleado,
                 nombres=profesor.nombres, apellidos=profesor.apellidos, horasClase=profesor.horasClase).where(profesores.c.id == id))
    return conn.execute(profesores.select().where(profesores.c.id == id)).first()
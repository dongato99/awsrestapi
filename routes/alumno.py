import boto3
from fastapi import APIRouter, HTTPException, UploadFile
from config.db import conn
from models.alumno import alumnos
from schemas.alumno import Alumno

alumno = APIRouter()


@alumno.get("/alumnos")
def get_alumnos():
    return conn.execute(alumnos.select()).fetchall()


@alumno.post('/alumnos', status_code=201)
def create_alumno(alumno: Alumno):
    new_alumno = {"nombres": alumno.nombres, "apellidos": alumno.apellidos,
                  "matricula": alumno.matricula, "promedio": alumno.promedio}
    result = conn.execute(alumnos.insert().values(new_alumno))
    return conn.execute(alumnos.select().where(alumnos.c.id == result.lastrowid)).first()


@alumno.get('/alumnos/{id}')
def get_alumno(id: str):
    return conn.execute(alumnos.select().where(alumnos.c.id == id)).first()


@alumno.delete('/alumnos/{id}')
def delete_alumno(id: str):
    conn.execute(alumnos.delete().where(alumnos.c.id == id))
    return {"message": "Alumno eliminado"}


@alumno.put('/alumnos/{id}')
def editar_alumno(id: str, alumno: Alumno):
    conn.execute(alumnos.update().values(nombres=alumno.nombres,
                 apellidos=alumno.apellidos, matricula=alumno.matricula, promedio=alumno.promedio).where(alumnos.c.id == id))
    return conn.execute(alumnos.select().where(alumnos.c.id == id)).first()
"""@alumno.get('/alumnos')
def get_alumnos():
    return alumnos

@alumno.get('/alumnos/{id}')
def get_alumno(id:int):
    for alumno in alumnos:
        if alumno["id"] == id:
            return alumno
    raise HTTPException(status_code=404,detail = "Not Found")



@alumno.post('/alumnos',status_code=201)
def guardar_alumno(alumno:Alumno):
    alumnos.append(alumno.dict())
    return alumnos[-1]
    

@alumno.delete('/alumnos/{id}')
def eliminar_alumno(id:int):
    for index,alumno in enumerate(alumnos):
        if alumno["id"] == id:
            alumnos.pop(index)
            return {"message":"Alumno eliminado"}
    raise HTTPException(status_code=404,detail = "Not Found")


@alumno.put('/alumnos/{id}')
def editar_alumno(id:int, actualizadoalumno:Alumno):
    for index,alumno in enumerate(alumnos):
        if alumno["id"] == id:
            alumnos[index]["nombres"] = actualizadoalumno.nombres
            alumnos[index]["apellido"] = actualizadoalumno.apellidos
            alumnos[index]["matricula"] = actualizadoalumno.matricula
            alumnos[index]["promedio"] = actualizadoalumno.promedio
            return alumno
    raise HTTPException(status_code=404,detail = "Not Found")"""

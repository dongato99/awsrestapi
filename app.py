
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse


app = FastAPI()




alumnos = []
maestros = []

#Alumno Model
class Alumno(BaseModel):
    id:int
    nombres: str
    apellidos: str
    matricula: str
    promedio: float

class Maestro(BaseModel):
    id:int
    numeroEmpleado: int
    nombres: str
    apellidos: str
    horasClase: int

@app.get('/')
def read_root():
    return RedirectResponse(url='/docs')


@app.get('/alumnos')
def get_alumnos():
    return alumnos

@app.get('/alumnos/{id}')
def get_alumno(id:int):
    for alumno in alumnos:
        if alumno["id"] == id:
            return alumno
    raise HTTPException(status_code=404,detail = "Not Found")



@app.post('/alumnos',status_code=201)
def guardar_alumno(alumno:Alumno):
    alumnos.append(alumno.dict())
    return alumnos[-1]
    

@app.delete('/alumnos/{id}')
def eliminar_alumno(id:int):
    for index,alumno in enumerate(alumnos):
        if alumno["id"] == id:
            alumnos.pop(index)
            return {"message":"Alumno eliminado"}
    raise HTTPException(status_code=404,detail = "Not Found")


@app.put('/alumnos/{id}')
def editar_alumno(id:int, actualizadoalumno:Alumno):
    for index,alumno in enumerate(alumnos):
        if alumno["id"] == id:
            alumnos[index]["nombres"] = actualizadoalumno.nombres
            alumnos[index]["apellido"] = actualizadoalumno.apellidos
            alumnos[index]["matricula"] = actualizadoalumno.matricula
            alumnos[index]["promedio"] = actualizadoalumno.promedio
            return alumno
    raise HTTPException(status_code=404,detail = "Not Found")



@app.get('/maestros')
def get_maestros():
    return maestros

@app.get('/maestros/{id}')
def get_maestro(id:int):
    for maestro in maestros:
        if maestro["id"] == id:
            return maestro
    raise HTTPException(status_code=404,detail = "Not Found")



@app.post('/maestros',status_code=201)
def guardar_maestro(maestro:Maestro):
    maestros.append(maestro.dict())
    return maestros[-1]

@app.delete('/maestros/{id}')
def eliminar_maestro(id:int):
    for index,maestro in enumerate(maestros):
        if maestro["id"] == id:
            maestros.pop(index)
            return {"message":"Maestro eliminado"}
    raise HTTPException(status_code=404,detail = "Not Found")


@app.put('/maestros/{id}')
def editar_maestro(id:int, actualizadomaestro:Maestro):
    for index,maestro in enumerate(maestros):
        if maestro["id"] == id:
            maestros[index]["numeroEmpleado"] = actualizadomaestro.numeroEmpleado
            maestros[index]["nombres"] = actualizadomaestro.nombres
            maestros[index]["apellidos"] = actualizadomaestro.apellidos
            maestros[index]["horasClase"] = actualizadomaestro.horasClase
            return maestro
    raise HTTPException(status_code=404,detail = "Not Found")





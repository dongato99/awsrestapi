import boto3
from fastapi import APIRouter, HTTPException, UploadFile
from config.db import conn
from models.alumno import alumnos
from schemas.alumno import Alumno



session = boto3.Session(
aws_access_key_id='ASIA4NQTIJ2DGOA63WFO',
aws_secret_access_key='cquQKCkKxGZYy7bxnOx1XPxQZwHxlIuKJhAOtoAo',
aws_session_token='FwoGZXIvYXdzENP//////////wEaDAHjDM/c/D6KoGzCgiLHAY4SEpn+20ZnCUZR9gLuVlrt2cYS7UvMm0TUCjXwzvpjwyuUQCX95tBgm0cHo3/ZvDYYWHZFz40H1f3tQhxGLyQW4gJu3D1Yrmi/T2zbKzeC9ax4PA9SEYPMP6eakOuILu9RrddVraO2h9XWTXCP81MsFAOTk4EIwkZxqXQoiwe/9kUolYJIAAi4659AEzgAsE2iXKu7H26HE5KyEQlC4VS8cjUtqe9Fa1T3LJ35sblx4szGmftM4/08yJDJNypK+Det3SNP38wouPe+lAYyLR5VPW477BnEdBGdC/ufHrCyhUuQwufhb1oDkX129Oy1HkeN+KGYDw1+GfHqqQ=='
)

alumno = APIRouter()


@alumno.get("/alumnos")
def get_alumnos():
    return conn.execute(alumnos.select()).fetchall()


@alumno.post('/alumnos', status_code=201)
def create_alumno(alumno: Alumno):
    new_alumno = {"nombres": alumno.nombres, "apellidos": alumno.apellidos,
                  "matricula": alumno.matricula, "promedio": alumno.promedio, "fotoPerfilUrl":alumno.fotoPerfilUrl}
    result = conn.execute(alumnos.insert().values(new_alumno))
    return conn.execute(alumnos.select().where(alumnos.c.id == result.lastrowid)).first()


@alumno.get('/alumnos/{id}')
def get_alumno(id: str):
    if conn.execute(alumnos.select().where(alumnos.c.id == id)).first() is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return conn.execute(alumnos.select().where(alumnos.c.id == id)).first()

@alumno.post('/alumnos/{id}/fotoPerfil')
def add_fotoPerfil(id: str, foto:UploadFile):

    s3 = session.resource("s3")
    bucket = s3.Bucket("fotoperfilp")
    bucket.upload_fileobj(foto.file, foto.filename)

    fotoPerfilUrl= f"https://fotoperfilp.s3.amazonaws.com/{foto.filename}"
    conn.execute(alumnos.update().
    values(fotoPerfilUrl=fotoPerfilUrl).
    where(alumnos.c.id == id))
    return {"fotoPerfilUrl": f"https://fotoperfilp.s3.amazonaws.com/{foto.filename}"}

@alumno.delete('/alumnos/{id}')
def delete_alumno(id: str):
    if conn.execute(alumnos.select().where(alumnos.c.id == id)).first() is None:
        raise HTTPException(status_code=404, detail="Item not found")

    conn.execute(alumnos.delete().where(alumnos.c.id == id)) 
    return {"message": "Alumno eliminado"}


@alumno.put('/alumnos/{id}')
def editar_alumno(id: str, alumno: Alumno):
    conn.execute(alumnos.update().values(nombres=alumno.nombres,
                 apellidos=alumno.apellidos, matricula=alumno.matricula, promedio=alumno.promedio).where(alumnos.c.id == id))
    return conn.execute(alumnos.select().where(alumnos.c.id == id)).first()

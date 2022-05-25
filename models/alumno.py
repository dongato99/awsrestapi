from sqlalchemy import Float, Integer, String, Table, Column
from config.db import meta, engine
"""
class Alumno(BaseModel):
    id:int
    nombres: str
    apellidos: str
    matricula: str
    promedio: float

"""
alumnos = Table("alumnos", meta, 
Column("id", Integer, primary_key=True), 
Column("nombres", String(255)), 
Column("apellidos", String(255)), 
Column("matricula", String(255)), 
Column("promedio", Float))

meta.create_all(engine)
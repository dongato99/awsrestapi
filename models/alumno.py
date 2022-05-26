from sqlalchemy import Float, Integer, String, Table, Column
from config.db import meta, engine

alumnos = Table("alumnos", meta, 
Column("id", Integer, primary_key=True), 
Column("nombres", String(255)), 
Column("apellidos", String(255)), 
Column("matricula", String(255)), 
Column("promedio", Float),
Column("fotoPerfilUrl", String(255)))

meta.create_all(engine)
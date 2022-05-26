from sqlalchemy import Integer, String, Table, Column
from config.db import meta, engine

profesores = Table("profesores", meta, 
Column("id", Integer, primary_key=True), 
Column("numeroEmpleado", Integer), 
Column("nombres", String(255)), 
Column("apellidos", String(255)), 
Column("horasClase", Integer))

meta.create_all(engine)
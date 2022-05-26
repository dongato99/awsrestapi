from typing import Optional
from pydantic import BaseModel

class Profesor(BaseModel):
    id: Optional[str]
    numeroEmpleado: int
    nombres: str
    apellidos: str
    horasClase: int
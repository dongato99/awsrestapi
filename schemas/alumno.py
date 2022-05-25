from typing import Optional
from pydantic import BaseModel

class Alumno(BaseModel):
    id: Optional[str]
    nombres: str
    apellidos: str
    matricula: str
    promedio: float

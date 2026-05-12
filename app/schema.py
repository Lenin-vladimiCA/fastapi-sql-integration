from pydantic import BaseModel
from typing import Optional

class Model_usuario(BaseModel):
    nombre:str
    apellido:str
    edad:int


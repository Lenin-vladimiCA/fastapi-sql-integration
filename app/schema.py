from pydantic import BaseModel
from typing import Optional

#Modelo:validacion de datos Usuario
class usuarioSchema(BaseModel):
    nombre: str
    apellido: str
    edad: int

#Modelo:validacion de datos Cliente
class clientesSchema(BaseModel):
    nombre:str
    apellido:str
    llegada:str
    Vuelo:str
    Cantidad:int
    Propian_A:str
    Propian_Ma:str
    Propina_M:str

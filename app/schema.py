from pydantic import BaseModel
from typing import Optional,List


#Modelo:validacion de datos Usuario
class usuarioSchema(BaseModel):
    nombre: str
    apellido: str
    edad: int

class LibroSchema(BaseModel):
    id:int
    nombre_libro:str
    cantidad:int
    Descripsion:str
    class Config:
        from_attributes = True
    


#Modelo:validacion de datos Cliente
class clientesSchema(BaseModel):
    nombre:str
    apellido:str
    libro:List[LibroSchema]= []
    cantidad:int
    class config:
        from_attributes=True




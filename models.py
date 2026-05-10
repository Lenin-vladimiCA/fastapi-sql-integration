from sqlalchemy import Column,String,Integer
from database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer,primary_key=True,autoincrement=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    edad = Column(Integer)

    
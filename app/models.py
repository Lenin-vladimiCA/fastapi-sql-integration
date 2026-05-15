from sqlalchemy import Column,String,Integer
from database import Base

class usuarioBase(Base):
    __tablename__ = "usuario"

    id = Column(Integer,primary_key=True,autoincrement=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    edad = Column(Integer)

class clienteBase(Base):
    __tablename__='cliente'

    id = Column(Integer,primary_key=True,autoincrement=True)
    nombre= Column(String(50),nullable=False)
    apellido = Column(String(50),nullable= False)
    llegada = Column(String(50))
    Vuelo = Column(String)
    Cantidad =Column(Integer)
    Propian_A = Column(String)
    Propian_Ma = Column(String)
    Propina_M = Column(String)
    


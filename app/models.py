from sqlalchemy import Column,String,Integer,ForeignKey,Table
from sqlalchemy.orm import relationship
from database import Base


#User
class usuarioBase(Base):
    __tablename__ = "usuario"

    id = Column(Integer,primary_key=True,autoincrement=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    edad = Column(Integer)



clientes_libro_asociacion = Table(
    'cliente libro',
    Base.metadata,
    Column('cliente_id',Integer,ForeignKey('cliente.id'),primary_key=True),
    Column('libros_id',Integer,ForeignKey('Libros.id'),primary_key=True)
)


#Costumer
class clienteBase(Base):
    __tablename__='cliente'

    id = Column(Integer,primary_key=True,autoincrement=True)
    nombre= Column(String(50),nullable=False)
    apellido = Column(String(50),nullable= False)
    Cantidad =Column(Integer)
    Descripsion = Column(String)
    libros = relationship('LibrosBase', secondary=clientes_libro_asociacion, back_populates='pedido')

#Books
class LibrosBase(Base):
    __tablename__ = 'Libros'
    
    id=Column(Integer,primary_key=True,autoincrement=True)
    nombre_libro = Column(String(50),nullable=False)
    cantidad= Column(Integer,default=0)
    Descripsion = Column(String)
    pedido = relationship('clienteBase',secondary=clientes_libro_asociacion,back_populates='libros')


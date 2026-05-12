#AQUI LLAMAREMOS LA BASE DE DATOS PARA QUE SE PUEDA CONECAR SQLITE O POSTGRES

from sqlalchemy.orm import sessionmaker,DeclarativeBase
from sqlalchemy import create_engine

url = "sqlite:///Practica.db"

engine = create_engine(url,echo=True,connect_args={'check_same_thread':False})
Sessionlocal  = sessionmaker(autocommit= False,autoflush=False,bind=engine)


class Base (DeclarativeBase):
    pass
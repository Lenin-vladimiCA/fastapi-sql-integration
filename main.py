from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
# Aquí quitamos el punto y agregamos "Base"
from database import Sessionlocal, engine, Base 
import models

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def Conexion():
    session = Sessionlocal()
    try:
        yield session
    finally:
        session.close()


@app.get("/usuarios",tags=['usuarios'])
def Get_usuarios(db:Session = Depends(Conexion)):
    return db.query(models.Usuario).all()



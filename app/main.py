from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Sessionlocal, engine, Base 
from schema import Model_usuario
import models

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def Conexion():
    session = Sessionlocal()
    try:
        yield session
    finally:
        session.close()

# Metodo Get
@app.get("/usuarios",tags=['usuarios'])
def Get_usuarios(db:Session = Depends(Conexion)):
    return db.query(models.Usuario).all()


# Metodo Post
@app.post("/Post_usuario",tags=['usuarios'])
def post_usuario(nombre:str,apellido:str,edad:int,db:Session=Depends(Conexion)):
    usuario_db = models.Usuario(nombre=nombre,apellido=apellido,edad=edad)
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db


#metodo Put
@app.put("/put_usuario/{id}",tags=['usuarios'])
def put_usuario(id:int,nombre:str,apellido:str,edad:int, db:Session = Depends(Conexion)):
     filtrado = db.query(models.Usuario).filter(models.Usuario.id == id).first()

     filtrado.nombre = nombre
     filtrado.apellido = apellido
     filtrado.edad = edad

     db.commit()
     db.refresh(filtrado)

     return filtrado

#metodo delete 
@app.delete('/delete_usuario',tags=['usuarios'])
def delete_usuario(id_u:int,db:Session=Depends(Conexion)):
    filtrado = db.query(models.Usuario).filter(models.Usuario.id == id_u).first()
    db.delete(filtrado)
    db.commit()

         

    
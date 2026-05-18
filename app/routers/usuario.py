from fastapi import HTTPException,APIRouter,Depends
from sqlalchemy.orm import Session
from schema import usuarioSchema
from models import usuarioBase
from database import Conexion



router = APIRouter(
    prefix='/usuario', tags=['Usuarios']
)


# Metodo Get
@router.get("/get_usuario",response_model=list[usuarioSchema])
def Get_usuarios(db:Session = Depends(Conexion)):
    return db.query(usuarioBase).all()


# Metodo Post
@router.post("/Post_usuario",response_model=usuarioSchema)
def post_usuario(nombre:str,apellido:str,edad:int,db:Session=Depends(Conexion)):
    usuario_db = usuarioBase(nombre=nombre,apellido=apellido,edad=edad)
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db


#metodo Put
@router.put("/put_usuario/{id}",response_model=usuarioSchema)
def put_usuario(edictUsuario:usuarioSchema,db:Session = Depends(Conexion)):
     filtrado = db.query(usuarioBase).filter(usuarioBase.id == id).first()

     filtrado.nombre = edictUsuario.nombre
     filtrado.apellido = edictUsuario.apellido
     filtrado.edad = edictUsuario.edad

     db.commit()
     db.refresh(filtrado)

     return filtrado

#metodo delete 
@router.delete('/delete_usuario',response_model=usuarioSchema)
def delete_usuario(id_u:int,db:Session=Depends(Conexion)):
    filtrado = db.query(usuarioBase).filter(usuarioBase.id == id_u).first()
    db.delete(filtrado)
    db.commit()

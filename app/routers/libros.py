from fastapi import APIRouter,Depends,FastAPI,HTTPException,status
from database import Conexion
from schema import LibroSchema
from models import LibrosBase
from sqlalchemy.orm import Session

app = FastAPI()

routerLibro = APIRouter(
    prefix="/Libros",tags=["Libros"]
)

@routerLibro.get('/get_libro',response_model=list[LibroSchema])
def get_libros(db:Session = Depends(Conexion)):
    return db.query(LibrosBase).all()

@routerLibro.post('/post_libro',response_model=LibroSchema)
def post_libro(Libro:LibroSchema, db:Session = Depends(Conexion)):
    agregado  = LibrosBase(**Libro.model_dump())
    db.add(agregado)
    db.commit()
    db.refresh(agregado)
    return agregado

@routerLibro.put('/put_libro',response_model=LibroSchema)
def put_libro(id:int,edictLibro:LibroSchema,db:Session = Depends(Conexion)):
    edictar = db.query(LibrosBase).filter(LibrosBase.id == id).first()
    
    if not edictar:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con id {id} no encontrado"
        )
    
    if edictar.id == id:
        edictar.nombre_libro = edictLibro.nombre_libro
        edictar.cantidad = edictLibro.cantidad
        edictar.Descripsion = edictLibro.Descripsion

    db.commit()
    db.refresh(edictar)
    return edictar

@routerLibro.delete('/delete_libro/{id}',response_model=LibroSchema)
def delete_libro(id:int,db:Session=Depends(Conexion)):
    eliminacion = db.query(LibrosBase).filter(LibrosBase.id == id).first()

    if not eliminacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El libro con el id {id} no existe."
        )
    
    db.delete(eliminacion)
    db.commit()
    return eliminacion
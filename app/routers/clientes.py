
from fastapi import Depends,APIRouter,FastAPI
from models import clienteBase
from schema import clientesSchema
from sqlalchemy.orm import Session
from database import Conexion

router = APIRouter(
    prefix='/cliente',tags=['Cliente']
)


#Metodo gets Cliente
@router.get('/get_cleinte',response_model=list[clientesSchema])
def getCliente(db:Session = Depends(Conexion)):
    return db.query(clienteBase).all()


@router.post('/post_cliente',response_model=clientesSchema)
def postCliente(Cliente:clientesSchema,db:Session=Depends(Conexion)):
    agregado =  clienteBase(**Cliente.model_dump())
    db.add(agregado)
    db.commit()
    db.refresh(agregado)
    return agregado

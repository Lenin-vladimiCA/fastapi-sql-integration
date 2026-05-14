from fastapi import FastAPI, Depends
from routers.usuario import router as router_usuario
from routers.clientes import router as router_cliente
from database import engine
import models as models

models.Base.metadata.create_all(bind = engine)

app = FastAPI()
app.include_router(router_cliente)
app.include_router(router_usuario)




    
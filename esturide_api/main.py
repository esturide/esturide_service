from fastapi import FastAPI

from esturide_api import models
from esturide_api.config.database import engine
from esturide_api.routers.auth import router as AuthorizationRouter
from esturide_api.routers.automobile import router as AutomobileRouter
from esturide_api.routers.drivers import router as DriverRouter
from esturide_api.routers.populate_db import router as DBRouter
from esturide_api.routers.user import router as UserRouter

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(UserRouter)
app.include_router(AuthorizationRouter)
app.include_router(DriverRouter)
app.include_router(AutomobileRouter)
app.include_router(DBRouter)


@app.get("/")
def read_root():
    return {"Hello": "World"}

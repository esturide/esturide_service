from fastapi import FastAPI, HTTPException

from app.shared.database import engine, Base
from app.services.user_management_system.contexts.user.domain.errors import UserServiceValidationError
from app.services.user_management_system.contexts.user.infraestructure.router.user_router import (
    router as v2_user_router,
)
from app.services.user_management_system.routers.auth import router as authorization_router
from app.services.user_management_system.routers.automobile import router as automobile_router
from app.services.user_management_system.routers.drivers import router as driver_router
from app.services.user_management_system.routers.user import router as user_router
from app.services.user_management_system.shared.authentication.infraestructure.router.authentication_router import (
    router as v2_authorization_router,
)

Base.metadata.create_all(bind=engine)
user_management_system_service = FastAPI(
    title="User Management System"
)

user_management_system_service.include_router(user_router)
user_management_system_service.include_router(authorization_router)
user_management_system_service.include_router(driver_router)
user_management_system_service.include_router(automobile_router)
user_management_system_service.include_router(v2_user_router)
user_management_system_service.include_router(v2_authorization_router)


@user_management_system_service.get("/")
def index():
    return {"message": "Hello World from 'User Management System'"}


@user_management_system_service.exception_handler(UserServiceValidationError)
def user_service_validation_exception_handler(request, exc: UserServiceValidationError):
    raise HTTPException(status_code=400, detail=str(exc))

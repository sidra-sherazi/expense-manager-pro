from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.user import (
    UserRegister,
    UserLogin,
    UserResponse,
)

from app.schemas.token import Token

from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
)
def register(
    data: UserRegister,
    db: Session = Depends(get_db),
):
    return AuthService.register(db, data)


@router.post(
    "/login",
    response_model=Token,
)
def login(
    data: UserLogin,
    db: Session = Depends(get_db),
):
    return AuthService.login(db, data)
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

from app.models.user import User

from app.repositories.user_repository import UserRepository

from app.schemas.user import (
    UserRegister,
    UserLogin,
)


class AuthService:

    @staticmethod
    def register(db: Session, data: UserRegister):

        if UserRepository.get_by_email(db, data.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists",
            )

        if UserRepository.get_by_username(db, data.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists",
            )

        user = User(
            username=data.username,
            email=data.email,
            hashed_password=hash_password(data.password),
        )

        return UserRepository.create(db, user)

    @staticmethod
    def login(db: Session, data: UserLogin):

        user = UserRepository.get_by_email(db, data.email)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password",
            )

        if not verify_password(
            data.password,
            user.hashed_password,
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password",
            )

        token = create_access_token(
            {"sub": str(user.id)}
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }
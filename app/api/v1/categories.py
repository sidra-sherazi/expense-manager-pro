from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse,
)
from app.services.category_service import CategoryService

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post(
    "/",
    response_model=CategoryResponse,
)
def create_category(
    data: CategoryCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return CategoryService.create(
        db,
        data,
        user,
    )


@router.get(
    "/",
    response_model=list[CategoryResponse],
)
def get_categories(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return CategoryService.get_all(
        db,
        user,
    )


@router.put(
    "/{category_id}",
    response_model=CategoryResponse,
)
def update_category(
    category_id: int,
    data: CategoryUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return CategoryService.update(
        db,
        category_id,
        data,
        user,
    )


@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return CategoryService.delete(
        db,
        category_id,
        user,
    )
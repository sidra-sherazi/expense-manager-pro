from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.category import Category
from app.models.user import User
from app.repositories.category_repository import CategoryRepository
from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
)


class CategoryService:

    @staticmethod
    def create(
        db: Session,
        data: CategoryCreate,
        user: User,
    ):

        existing = CategoryRepository.get_by_name(
            db,
            data.name,
            user.id,
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Category already exists",
            )

        category = Category(
            name=data.name,
            user_id=user.id,
        )

        return CategoryRepository.create(
            db,
            category,
        )

    @staticmethod
    def get_all(
        db: Session,
        user: User,
    ):
        return CategoryRepository.get_all(
            db,
            user.id,
        )

    @staticmethod
    def update(
        db: Session,
        category_id: int,
        data: CategoryUpdate,
        user: User,
    ):

        category = CategoryRepository.get_by_id(
            db,
            category_id,
            user.id,
        )

        if category is None:
            raise HTTPException(
                status_code=404,
                detail="Category not found",
            )

        duplicate = CategoryRepository.get_by_name(
            db,
            data.name,
            user.id,
        )

        if duplicate and duplicate.id != category.id:
            raise HTTPException(
                status_code=400,
                detail="Category already exists",
            )

        category.name = data.name

        db.commit()
        db.refresh(category)

        return category

    @staticmethod
    def delete(
        db: Session,
        category_id: int,
        user: User,
    ):

        category = CategoryRepository.get_by_id(
            db,
            category_id,
            user.id,
        )

        if category is None:
            raise HTTPException(
                status_code=404,
                detail="Category not found",
            )

        CategoryRepository.delete(
            db,
            category,
        )

        return {
            "message": "Category deleted successfully"
        }
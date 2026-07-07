from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.expense import Expense
from app.models.user import User
from datetime import date

from app.repositories.category_repository import CategoryRepository
from app.repositories.expense_repository import ExpenseRepository


from app.schemas.expense import (
    ExpenseCreate,
    ExpenseUpdate,
)


class ExpenseService:

    @staticmethod
    def create(
        db: Session,
        data: ExpenseCreate,
        user: User,
    ):

        category = CategoryRepository.get_by_id(
            db=db,
            category_id=data.category_id,
            user_id=user.id,
        )

        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found",
            )

        expense = Expense(
            title=data.title,
            amount=data.amount,
            description=data.description,
            category_id=data.category_id,
            user_id=user.id,
        )

        return ExpenseRepository.create(
            db=db,
            expense=expense,
        )

    @staticmethod
    def get_all(
        db: Session,
        user: User,
        category_id: int | None = None,
        min_amount: float | None = None,
        max_amount: float | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
        sort: str | None = None,
        page: int = 1,
        page_size: int = 10,
    ):
        return ExpenseRepository.get_all(
            db=db,
            user_id=user.id,
            category_id=category_id,
            min_amount=min_amount,
            max_amount=max_amount,
            start_date=start_date,
            end_date=end_date,
            sort=sort,
            page=page,
            page_size=page_size,
        )

    @staticmethod
    def get_by_id(
        db: Session,
        expense_id: int,
        user: User,
    ):

        expense = ExpenseRepository.get_by_id(
            db=db,
            expense_id=expense_id,
            user_id=user.id,
        )

        if expense is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Expense not found",
            )

        return expense

    @staticmethod
    def update(
        db: Session,
        expense_id: int,
        data: ExpenseUpdate,
        user: User,
    ):

        expense = ExpenseRepository.get_by_id(
            db=db,
            expense_id=expense_id,
            user_id=user.id,
        )

        if expense is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Expense not found",
            )

        category = CategoryRepository.get_by_id(
            db=db,
            category_id=data.category_id,
            user_id=user.id,
        )

        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found",
            )

        expense.title = data.title
        expense.amount = data.amount
        expense.description = data.description
        expense.category_id = data.category_id

        return ExpenseRepository.update(
            db=db,
            expense=expense,
        )

    @staticmethod
    def delete(
        db: Session,
        expense_id: int,
        user: User,
    ):

        expense = ExpenseRepository.get_by_id(
            db=db,
            expense_id=expense_id,
            user_id=user.id,
        )

        if expense is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Expense not found",
            )

        ExpenseRepository.delete(
            db=db,
            expense=expense,
        )

        return {
            "message": "Expense deleted successfully"
        }
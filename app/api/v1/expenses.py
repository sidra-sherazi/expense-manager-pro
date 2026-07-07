from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from datetime import date
from app.db.session import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.expense import (
    ExpenseCreate,
    ExpenseUpdate,
    ExpenseResponse,
    ExpenseListResponse
)

from app.services.expense_service import ExpenseService

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"],
)


@router.post(
    "/",
    response_model=ExpenseResponse,
)
def create_expense(
    data: ExpenseCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ExpenseService.create(
        db,
        data,
        user,
    )


@router.get(
    "/",
    response_model=ExpenseListResponse,
)
def get_expenses(
    category_id: int | None = None,
    min_amount: float | None = None,
    max_amount: float | None = None,
    start_date: date | None = None,
    end_date: date | None = None,
    sort: str | None = None,
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ExpenseService.get_all(
        db=db,
        user=user,
        category_id=category_id,
        min_amount=min_amount,
        max_amount=max_amount,
        start_date=start_date,
        end_date=end_date,
        sort=sort,
        page=page,
        page_size=page_size,
    )


@router.get(
    "/{expense_id}",
    response_model=ExpenseResponse,
)
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ExpenseService.get_by_id(
        db,
        expense_id,
        user,
    )


@router.put(
    "/{expense_id}",
    response_model=ExpenseResponse,
)
def update_expense(
    expense_id: int,
    data: ExpenseUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ExpenseService.update(
        db,
        expense_id,
        data,
        user,
    )


@router.delete("/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ExpenseService.delete(
        db,
        expense_id,
        user,
    )
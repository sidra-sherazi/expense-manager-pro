from datetime import date

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User

from app.schemas.expense import (
    ExpenseCreate,
    ExpenseUpdate,
    ExpenseResponse,
    ExpenseListResponse,
)

from app.services.expense_service import ExpenseService

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"],
)


@router.post(
    "/",
    response_model=ExpenseResponse,
    summary="Create Expense",
    description="Create a new expense for the authenticated user.",
)
def create_expense(
    data: ExpenseCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ExpenseService.create(
        db=db,
        data=data,
        user=user,
    )


@router.get(
    "/",
    response_model=ExpenseListResponse,
    summary="Get Expenses",
    description="Retrieve expenses with filtering, searching, sorting, and pagination.",
)
def get_expenses(
    category_id: int | None = Query(
        default=None,
        description="Filter by category ID",
    ),
    min_amount: float | None = Query(
        default=None,
        description="Minimum expense amount",
    ),
    max_amount: float | None = Query(
        default=None,
        description="Maximum expense amount",
    ),
    start_date: date | None = Query(
        default=None,
        description="Filter expenses created on or after this date",
    ),
    end_date: date | None = Query(
        default=None,
        description="Filter expenses created on or before this date",
    ),
    search: str | None = Query(
        default=None,
        description="Search by title or description",
    ),
    sort_by: str = Query(
        default="created_at",
        description="Sort by: created_at, amount, title",
    ),
    order: str = Query(
        default="desc",
        description="Sort order: asc or desc",
    ),
    page: int = Query(
        default=1,
        ge=1,
        description="Page number",
    ),
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
        description="Number of records per page",
    ),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ExpenseService.get_all(
        db=db,
        user=user,
        search=search,
        category_id=category_id,
        min_amount=min_amount,
        max_amount=max_amount,
        start_date=start_date,
        end_date=end_date,
        sort_by=sort_by,
        order=order,
        page=page,
        limit=limit,
    )


@router.get(
    "/{expense_id}",
    response_model=ExpenseResponse,
    summary="Get Expense",
    description="Retrieve a single expense by its ID.",
)
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ExpenseService.get_by_id(
        db=db,
        expense_id=expense_id,
        user=user,
    )


@router.put(
    "/{expense_id}",
    response_model=ExpenseResponse,
    summary="Update Expense",
    description="Update an existing expense.",
)
def update_expense(
    expense_id: int,
    data: ExpenseUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ExpenseService.update(
        db=db,
        expense_id=expense_id,
        data=data,
        user=user,
    )


@router.delete(
    "/{expense_id}",
    summary="Delete Expense",
    description="Delete an expense by its ID.",
)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ExpenseService.delete(
        db=db,
        expense_id=expense_id,
        user=user,
    )
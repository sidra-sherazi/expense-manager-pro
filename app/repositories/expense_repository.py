from datetime import date

from sqlalchemy import func, or_
from sqlalchemy.orm import Session

from app.models.expense import Expense


class ExpenseRepository:

    @staticmethod
    def create(
        db: Session,
        expense: Expense,
    ):
        db.add(expense)
        db.commit()
        db.refresh(expense)
        return expense

    @staticmethod
    def get_all(
        db: Session,
        user_id: int,
        search: str | None = None,
        category_id: int | None = None,
        min_amount: float | None = None,
        max_amount: float | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
        sort_by: str = "created_at",
        order: str = "desc",
        page: int = 1,
        limit: int = 10,
    ):

        query = db.query(Expense).filter(
            Expense.user_id == user_id,
        )

        # Search
        if search:
            query = query.filter(
                or_(
                    Expense.title.ilike(f"%{search}%"),
                    Expense.description.ilike(f"%{search}%"),
                )
            )

        # Category Filter
        if category_id is not None:
            query = query.filter(
                Expense.category_id == category_id,
            )

        # Minimum Amount
        if min_amount is not None:
            query = query.filter(
                Expense.amount >= min_amount,
            )

        # Maximum Amount
        if max_amount is not None:
            query = query.filter(
                Expense.amount <= max_amount,
            )

        # Date Range
        if start_date is not None:
            query = query.filter(
                func.date(Expense.created_at) >= start_date,
            )

        if end_date is not None:
            query = query.filter(
                func.date(Expense.created_at) <= end_date,
            )

        total = query.count()

        # Sorting
        sortable_columns = {
            "created_at": Expense.created_at,
            "amount": Expense.amount,
            "title": Expense.title,
        }

        sort_column = sortable_columns.get(
            sort_by,
            Expense.created_at,
        )

        if order.lower() == "asc":
            query = query.order_by(
                sort_column.asc(),
            )
        else:
            query = query.order_by(
                sort_column.desc(),
            )

        # Pagination
        expenses = (
            query
            .offset((page - 1) * limit)
            .limit(limit)
            .all()
        )

        pages = (
            (total + limit - 1) // limit
            if total > 0
            else 0
        )

        return {
            "items": expenses,
            "total": total,
            "page": page,
            "limit": limit,
            "pages": pages,
        }

    @staticmethod
    def get_by_id(
        db: Session,
        expense_id: int,
        user_id: int,
    ):
        return (
            db.query(Expense)
            .filter(
                Expense.id == expense_id,
                Expense.user_id == user_id,
            )
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        expense: Expense,
    ):
        db.commit()
        db.refresh(expense)
        return expense

    @staticmethod
    def delete(
        db: Session,
        expense: Expense,
    ):
        db.delete(expense)
        db.commit()
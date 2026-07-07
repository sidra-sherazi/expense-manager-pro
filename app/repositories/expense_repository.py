from sqlalchemy.orm import Session
from app.models.expense import Expense
from datetime import date
from sqlalchemy import func


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
        category_id: int | None = None,
        min_amount: float | None = None,
        max_amount: float | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
        sort: str | None = None,
        page: int = 1,
        page_size: int = 10,
    ):

        query = db.query(Expense).filter(
            Expense.user_id == user_id,
        )

        if category_id:
            query = query.filter(
                Expense.category_id == category_id,
            )

        if min_amount is not None:
            query = query.filter(
                Expense.amount >= min_amount,
            )

        if max_amount is not None:
            query = query.filter(
                Expense.amount <= max_amount,
            )

        if start_date:
            query = query.filter(
                func.date(Expense.created_at) >= start_date,
            )

        if end_date:
            query = query.filter(
                func.date(Expense.created_at) <= end_date,
            )

        total = query.count()

        if sort == "amount_asc":
            query = query.order_by(
                Expense.amount.asc(),
            )

        elif sort == "amount_desc":
            query = query.order_by(
                Expense.amount.desc(),
            )

        elif sort == "oldest":
            query = query.order_by(
                Expense.created_at.asc(),
            )

        else:
            query = query.order_by(
                Expense.created_at.desc(),
            )

        expenses = (
            query
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return {
            "total": total,
            "page": page,
            "page_size": page_size,
            "items": expenses,
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
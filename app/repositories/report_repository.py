from sqlalchemy import extract
from sqlalchemy import func
from sqlalchemy.orm import Session
from calendar import month_name
from app.models.category import Category
from app.models.expense import Expense


class ReportRepository:

    @staticmethod
    def monthly_report(
        db: Session,
        user_id: int,
    ):
        result = (
            db.query(
                extract("month", Expense.created_at).label("month"),
                func.sum(Expense.amount).label("total"),
            )
            .filter(Expense.user_id == user_id)
            .group_by(extract("month", Expense.created_at))
            .order_by(extract("month", Expense.created_at))
            .all()
        )

        return [
            {
                "month": month_name[int(row.month)],
                "total": float(row.total),
            }
            for row in result
        ]

    @staticmethod
    def yearly_report(
        db: Session,
        user_id: int,
    ):
        return (
            db.query(
                extract("year", Expense.created_at).label("year"),
                func.sum(Expense.amount).label("total"),
            )
            .filter(
                Expense.user_id == user_id,
            )
            .group_by(
                extract("year", Expense.created_at),
            )
            .order_by(
                extract("year", Expense.created_at),
            )
            .all()
        )

    @staticmethod
    def category_report(
        db: Session,
        user_id: int,
    ):
        return (
            db.query(
                Category.name.label("category"),
                func.sum(Expense.amount).label("total"),
            )
            .join(
                Expense,
                Expense.category_id == Category.id,
            )
            .filter(
                Expense.user_id == user_id,
            )
            .group_by(
                Category.name,
            )
            .order_by(
                func.sum(Expense.amount).desc(),
            )
            .all()
        )
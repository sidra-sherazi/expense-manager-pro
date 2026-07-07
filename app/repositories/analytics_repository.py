from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.category import Category
from app.models.expense import Expense


class AnalyticsRepository:

    @staticmethod
    def summary(
        db: Session,
        user_id: int,
    ):
        return (
            db.query(
                func.count(Expense.id),
                func.sum(Expense.amount),
                func.avg(Expense.amount),
                func.max(Expense.amount),
                func.min(Expense.amount),
            )
            .filter(
                Expense.user_id == user_id
            )
            .first()
        )

    @staticmethod
    def category_summary(
        db: Session,
        user_id: int,
    ):
        return (
            db.query(
                Category.name,
                func.sum(Expense.amount).label("total"),
            )
            .join(
                Expense,
                Expense.category_id == Category.id,
            )
            .filter(
                Expense.user_id == user_id,
            )
            .group_by(Category.name)
            .order_by(
                func.sum(Expense.amount).desc()
            )
            .all()
        )
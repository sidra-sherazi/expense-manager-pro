from datetime import datetime, timedelta

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.category import Category
from app.models.expense import Expense


class DashboardRepository:

    @staticmethod
    def get_dashboard(db: Session, user_id: int):

        now = datetime.utcnow()

        today = now.date()

        week_start = now - timedelta(days=7)

        month_start = now.replace(
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

        total_expenses = (
            db.query(func.coalesce(func.sum(Expense.amount), 0))
            .filter(Expense.user_id == user_id)
            .scalar()
        )

        expenses_today = (
            db.query(func.coalesce(func.sum(Expense.amount), 0))
            .filter(
                Expense.user_id == user_id,
                func.date(Expense.created_at) == today,
            )
            .scalar()
        )

        expenses_week = (
            db.query(func.coalesce(func.sum(Expense.amount), 0))
            .filter(
                Expense.user_id == user_id,
                Expense.created_at >= week_start,
            )
            .scalar()
        )

        expenses_month = (
            db.query(func.coalesce(func.sum(Expense.amount), 0))
            .filter(
                Expense.user_id == user_id,
                Expense.created_at >= month_start,
            )
            .scalar()
        )

        highest_expense = (
            db.query(func.max(Expense.amount))
            .filter(Expense.user_id == user_id)
            .scalar()
            or 0
        )

        total_categories = (
            db.query(Category)
            .filter(Category.user_id == user_id)
            .count()
        )

        total_records = (
            db.query(Expense)
            .filter(Expense.user_id == user_id)
            .count()
        )

        return {
            "total_expenses": total_expenses,
            "expenses_today": expenses_today,
            "expenses_this_week": expenses_week,
            "expenses_this_month": expenses_month,
            "total_categories": total_categories,
            "total_expense_records": total_records,
            "highest_expense": highest_expense,
        }
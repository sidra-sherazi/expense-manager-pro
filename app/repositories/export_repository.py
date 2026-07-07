from sqlalchemy.orm import Session

from app.models.expense import Expense
from app.models.category import Category


class ExportRepository:

    @staticmethod
    def get_expenses(
        db: Session,
        user_id: int,
    ):
        return (
            db.query(
                Expense.title,
                Expense.amount,
                Category.name.label("category"),
                Expense.description,
                Expense.created_at,
            )
            .join(
                Category,
                Expense.category_id == Category.id,
            )
            .filter(
                Expense.user_id == user_id,
            )
            .order_by(
                Expense.created_at.desc(),
            )
            .all()
        )
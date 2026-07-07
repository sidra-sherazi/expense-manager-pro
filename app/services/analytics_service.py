from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.analytics_repository import AnalyticsRepository


class AnalyticsService:

    @staticmethod
    def summary(
        db: Session,
        user: User,
    ):
        result = AnalyticsRepository.summary(
            db=db,
            user_id=user.id,
        )

        return {
            "total_expenses": result[0] or 0,
            "total_amount": result[1] or 0,
            "average_amount": result[2] or 0,
            "highest_expense": result[3] or 0,
            "lowest_expense": result[4] or 0,
        }

    @staticmethod
    def category_summary(
        db: Session,
        user: User,
    ):
        rows = AnalyticsRepository.category_summary(
            db=db,
            user_id=user.id,
        )

        return [
            {
                "category": row[0],
                "total": row[1],
            }
            for row in rows
        ]
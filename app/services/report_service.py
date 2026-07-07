from sqlalchemy.orm import Session

from app.models.user import User

from app.repositories.report_repository import ReportRepository


class ReportService:

    @staticmethod
    def monthly_report(
        db: Session,
        user: User,
    ):
        return ReportRepository.monthly_report(
            db=db,
            user_id=user.id,
        )

    @staticmethod
    def yearly_report(
        db: Session,
        user: User,
    ):
        return ReportRepository.yearly_report(
            db=db,
            user_id=user.id,
        )

    @staticmethod
    def category_report(
        db: Session,
        user: User,
    ):
        return ReportRepository.category_report(
            db=db,
            user_id=user.id,
        )
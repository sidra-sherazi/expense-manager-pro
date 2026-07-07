from sqlalchemy.orm import Session

from app.models.user import User

from app.repositories.dashboard_repository import DashboardRepository


class DashboardService:

    @staticmethod
    def get_dashboard(
        db: Session,
        user: User,
    ):
        return DashboardRepository.get_dashboard(
            db=db,
            user_id=user.id,
        )
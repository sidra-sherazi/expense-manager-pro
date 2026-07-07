from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.schemas.analytics import CategorySummary
from app.db.session import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.analytics import AnalyticsSummary
from app.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/summary",
    response_model=AnalyticsSummary,
)
def summary(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):

    return AnalyticsService.summary(
        db=db,
        user=user,
    )

@router.get(
    "/category-summary",
    response_model=list[CategorySummary],
)
def category_summary(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return AnalyticsService.category_summary(
        db=db,
        user=user,
    )
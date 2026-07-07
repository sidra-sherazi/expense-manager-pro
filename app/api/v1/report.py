from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.report import (
    MonthlyReportResponse,
    YearlyReportResponse,
    CategoryReportResponse,
)

from app.services.report_service import ReportService


router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.get(
    "/monthly",
    response_model=list[MonthlyReportResponse],
)
def monthly_report(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ReportService.monthly_report(
        db=db,
        user=user,
    )


@router.get(
    "/yearly",
    response_model=list[YearlyReportResponse],
)
def yearly_report(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ReportService.yearly_report(
        db=db,
        user=user,
    )


@router.get(
    "/category",
    response_model=list[CategoryReportResponse],
)
def category_report(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return ReportService.category_report(
        db=db,
        user=user,
    )
from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.services.export_service import ExportService

router = APIRouter(
    prefix="/export",
    tags=["Export"],
)


@router.get("/csv")
def export_csv(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):

    file_path = ExportService.export_csv(
        db=db,
        user=user,
    )

    return FileResponse(
        path=file_path,
        filename="expenses.csv",
        media_type="text/csv",
    )


@router.get("/excel")
def export_excel(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):

    file_path = ExportService.export_excel(
        db=db,
        user=user,
    )

    return FileResponse(
        path=file_path,
        filename="expenses.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
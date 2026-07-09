from fastapi import FastAPI
from app.api.v1.categories import router as category_router
from app.db.base import Base
from app.db.database import engine
from app.dependencies.auth import get_current_user
from app.models.user import User
from fastapi import Depends
from app.api.v1.expenses import router as expense_router
from app.api.v1.analytics import router as analytics_router
from app.api.v1.dashboard import router as dashboard_router
from app.api.v1.report import router as report_router
from app.api.v1.export import router as export_router
import app.models
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.auth import router as auth_router

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Expense Manager Pro",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(category_router)
app.include_router(expense_router)
app.include_router(analytics_router)
app.include_router(dashboard_router)
app.include_router(report_router)
app.include_router(export_router)


@app.get("/")
def root():
    return {"message": "Expense Manager Pro API"}


@app.get("/me")
def current_user(
    user: User = Depends(get_current_user),
):
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
    }

from fastapi import FastAPI

from app.db.base import Base
from app.db.database import engine

import app.models

from app.api.v1.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Manager Pro",
    version="1.0.0",
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Expense Manager Pro API"}
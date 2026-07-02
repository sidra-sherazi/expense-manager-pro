from fastapi import FastAPI

from app.db.base import Base
from app.db.database import engine

import app.models


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Manager Pro",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Expense Manager Pro API"
    }
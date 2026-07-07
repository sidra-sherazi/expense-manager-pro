from datetime import datetime
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict


class ExpenseCreate(BaseModel):
    title: str
    amount: float
    description: str | None = None
    category_id: int


class ExpenseUpdate(BaseModel):
    title: str
    amount: float
    description: str | None = None
    category_id: int


class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    description: str | None
    created_at: datetime
    category_id: int

    model_config = ConfigDict(
        from_attributes=True,
    )


class ExpenseListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[ExpenseResponse]

    model_config = {
        "from_attributes": True,
    }
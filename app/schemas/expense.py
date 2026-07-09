from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ExpenseCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=150,
        description="Expense title",
        examples=["Lunch"],
    )

    amount: float = Field(
        ...,
        gt=0,
        description="Expense amount",
        examples=[250.50],
    )

    description: str | None = Field(
        default=None,
        max_length=500,
        description="Expense description",
        examples=["Lunch with client"],
    )

    category_id: int = Field(
        ...,
        gt=0,
        description="Category ID",
        examples=[1],
    )


class ExpenseUpdate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=150,
    )

    amount: float = Field(
        ...,
        gt=0,
    )

    description: str | None = Field(
        default=None,
        max_length=500,
    )

    category_id: int = Field(
        ...,
        gt=0,
    )


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
    items: list[ExpenseResponse]
    total: int
    page: int
    limit: int
    pages: int

    model_config = ConfigDict(
        from_attributes=True,
    )
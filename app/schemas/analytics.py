from pydantic import BaseModel


class AnalyticsSummary(BaseModel):
    total_expenses: int
    total_amount: float
    average_amount: float
    highest_expense: float
    lowest_expense: float


class CategorySummary(BaseModel):
    category: str
    total: float


class MonthlySummary(BaseModel):
    month: str
    total: float
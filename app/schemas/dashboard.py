from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_expenses: float
    expenses_today: float
    expenses_this_week: float
    expenses_this_month: float
    total_categories: int
    total_expense_records: int
    highest_expense: float

    model_config = {
        "from_attributes": True,
    }
from pydantic import BaseModel


class MonthlyReportResponse(BaseModel):
    month: str
    total: float


class YearlyReportResponse(BaseModel):
    year: int
    total: float


class CategoryReportResponse(BaseModel):
    category: str
    total: float

    model_config = {
        "from_attributes": True,
    }
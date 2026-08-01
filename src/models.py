from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class ExpenseCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=1, max_length=50)
    date: date


class Expense(ExpenseCreate):
    id: int


class TotalResponse(BaseModel):
    total: float
    category: str | None = None


class MessageResponse(BaseModel):
    message: str
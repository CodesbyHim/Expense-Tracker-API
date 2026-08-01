from fastapi import APIRouter, HTTPException, status

from src.models import (
    Expense,
    ExpenseCreate,
    MessageResponse,
    TotalResponse,
)
from src.storage import add_expense, delete_expense, load_expenses

router = APIRouter()


@router.get("/", tags=["Home"])
def root():
    return {"message": "Welcome to the Smart Expense Tracker API!"}


@router.post(
    "/expenses",
    response_model=Expense,
    status_code=status.HTTP_201_CREATED,
    tags=["Expenses"],
    summary="Add a new expense",
)
def create_expense(expense: ExpenseCreate):
    return add_expense(expense)


@router.get(
    "/expenses",
    response_model=list[Expense],
    tags=["Expenses"],
    summary="View all expenses",
)
def get_expenses(category: str | None = None):
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    return expenses


@router.get(
    "/expenses/total",
    response_model=TotalResponse,
    response_model_exclude_none=True,
    tags=["Expenses"],
    summary="Calculate total expenses",
)
def get_total(category: str | None = None):
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    total = round(sum(expense["amount"] for expense in expenses), 2)

    if category:
        return TotalResponse(
            category=category,
            total=total,
        )

    return TotalResponse(total=total)


@router.delete(
    "/expenses/{expense_id}",
    response_model=MessageResponse,
    tags=["Expenses"],
    summary="Delete an expense",
    responses={
        404: {"description": "Expense not found"}
    },
)
def remove_expense(expense_id: int):
    deleted = delete_expense(expense_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found",
        )

    return MessageResponse(
        message="Expense deleted successfully"
    )
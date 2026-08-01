from fastapi import APIRouter, HTTPException

from src.models import Expense, ExpenseCreate
from src.storage import (
    add_expense,
    delete_expense,
    load_expenses,
)

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Welcome to the Smart Expense Tracker API!"}


@router.post("/expenses", response_model=Expense, status_code=201)
def create_expense(expense: ExpenseCreate):
    return add_expense(expense)


@router.get("/expenses", response_model=list[Expense])
def get_expenses(category: str | None = None):
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    return expenses


@router.get("/expenses/total")
def get_total(category: str | None = None):
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    total = sum(expense["amount"] for expense in expenses)

    if category:
        return {
            "category": category,
            "total": total,
        }

    return {
        "total": total,
    }


@router.delete("/expenses/{expense_id}")
def remove_expense(expense_id: int):
    deleted = delete_expense(expense_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return {
        "message": "Expense deleted successfully"
    }
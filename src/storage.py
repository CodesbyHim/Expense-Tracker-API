import json
from pathlib import Path

from src.models import Expense, ExpenseCreate

DATA_FILE = Path(__file__).parent / "data.json"


def load_expenses() -> list[dict]:
    """Load all expenses from the JSON file."""

    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        return []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_expenses(expenses: list[dict]) -> None:
    """Save all expenses to the JSON file."""

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def get_next_id(expenses: list[dict]) -> int:
    """Generate the next available expense ID."""

    if not expenses:
        return 1

    return max(expense["id"] for expense in expenses) + 1


def add_expense(expense: ExpenseCreate) -> Expense:
    """Add a new expense."""

    expenses = load_expenses()

    new_expense = Expense(
        id=get_next_id(expenses),
        **expense.model_dump(),
    )

    expenses.append(new_expense.model_dump(mode="json"))

    save_expenses(expenses)

    return new_expense


def delete_expense(expense_id: int) -> bool:
    """Delete an expense by ID."""

    expenses = load_expenses()

    updated_expenses = [
        expense
        for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        return False

    save_expenses(updated_expenses)

    return True
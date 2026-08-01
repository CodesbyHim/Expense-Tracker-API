import json
from pathlib import Path

from src.models import Expense, ExpenseCreate

# Path to the JSON file
DATA_FILE = Path(__file__).parent / "data.json"


def load_expenses():
    """Load all expenses from the JSON file."""
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    """Save all expenses to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def get_next_id(expenses):
    """Generate the next expense ID."""
    if not expenses:
        return 1
    return max(expense["id"] for expense in expenses) + 1


def add_expense(expense: ExpenseCreate):
    """Add a new expense to the JSON file."""
    expenses = load_expenses()

    new_expense = Expense(
        id=get_next_id(expenses),
        **expense.model_dump()
    )

    expenses.append(new_expense.model_dump(mode="json"))
    save_expenses(expenses)

    return new_expense


def delete_expense(expense_id: int):
    """Delete an expense by ID."""
    expenses = load_expenses()

    updated_expenses = [
        expense for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        return False

    save_expenses(updated_expenses)
    return True
import json
from pathlib import Path

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

DATA_FILE = Path(__file__).parent.parent / "src" / "data.json"


def reset_data():
    with open(DATA_FILE, "w") as file:
        json.dump([], file)


def test_add_expense():
    reset_data()

    response = client.post(
        "/expenses",
        json={
            "title": "Coffee",
            "amount": 150,
            "category": "Food",
            "date": "2026-08-02"
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Coffee"


def test_get_expenses():
    reset_data()

    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 300,
            "category": "Food",
            "date": "2026-08-02"
        }
    )

    response = client.get("/expenses")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_filter_by_category():
    reset_data()

    client.post(
        "/expenses",
        json={
            "title": "Bus",
            "amount": 100,
            "category": "Travel",
            "date": "2026-08-02"
        }
    )

    response = client.get("/expenses?category=Travel")

    assert response.status_code == 200
    assert response.json()[0]["category"] == "Travel"


def test_total_expenses():
    reset_data()

    client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-08-02"
        }
    )

    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json()["total"] == 250


def test_delete_expense():
    reset_data()

    client.post(
        "/expenses",
        json={
            "title": "Tea",
            "amount": 50,
            "category": "Food",
            "date": "2026-08-02"
        }
    )

    response = client.delete("/expenses/1")

    assert response.status_code == 200
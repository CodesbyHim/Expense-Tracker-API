import json

import pytest
from fastapi.testclient import TestClient

import src.storage as storage
from src.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def use_temp_data_file(tmp_path, monkeypatch):
    """
    Create a temporary data.json file for each test.
    This prevents tests from modifying the real data.json.
    """
    data_file = tmp_path / "data.json"
    data_file.write_text("[]", encoding="utf-8")

    monkeypatch.setattr(storage, "DATA_FILE", data_file)


def test_add_expense():
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


def test_reject_negative_amount():
    response = client.post(
        "/expenses",
        json={
            "title": "Invalid",
            "amount": -10,
            "category": "Food",
            "date": "2026-08-02"
        }
    )

    assert response.status_code == 422


def test_delete_nonexistent_expense():
    response = client.delete("/expenses/999")

    assert response.status_code == 404
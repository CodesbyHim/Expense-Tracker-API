# Smart Expense Tracker API

A simple REST API built with **FastAPI** to manage personal expenses. The application stores data in a local JSON file and provides endpoints to add, view, filter, calculate totals, and delete expenses.

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate total expenses by category
- Delete an expense
- Interactive Swagger/OpenAPI documentation
- Automated tests using pytest

## Project Structure

```
expense-tracker-api/
│── README.md
│── AI_NOTES.md
│── requirements.txt
│
├── src/
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── storage.py
│   └── data.json
│
└── tests/
    └── test_api.py
```

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd expense-tracker-api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```powershell
.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Server

```bash
uvicorn src.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
pytest
```

## Example Request

POST `/expenses`

```json
{
  "title": "Coffee",
  "amount": 150,
  "category": "Food",
  "date": "2026-08-02"
}
```

Example Response:

```json
{
  "id": 1,
  "title": "Coffee",
  "amount": 150,
  "category": "Food",
  "date": "2026-08-02"
}
```

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- JSON file storage

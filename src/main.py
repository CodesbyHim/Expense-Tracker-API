from fastapi import FastAPI
from src.routes import router

app = FastAPI(
    title="Smart Expense Tracker API",
    description="A simple REST API to manage personal expenses.",
    version="1.0.0"
)

app.include_router(router)
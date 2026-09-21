from fastapi import FastAPI, HTTPException
from datetime import date
import mysql.connector
try:
    from . import db_helper
except ImportError:
    import db_helper
from typing import List
from pydantic import BaseModel, Field, validator

app = FastAPI()


class Expense(BaseModel):
    id: int | None = None
    amount: float = Field(gt=0)
    category: str = Field(min_length=1, max_length=255)
    notes: str = Field(default="", max_length=1000)

    @validator("category")
    def category_must_not_be_blank(cls, value):
        value = value.strip()
        if not value:
            raise ValueError("Category must not be blank")
        return value


class DateRange(BaseModel):
    start_date: date
    end_date: date

    @validator("end_date")
    def end_date_must_not_precede_start_date(cls, value, values):
        if "start_date" in values and value < values["start_date"]:
            raise ValueError("End date must be on or after start date")
        return value


@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    try:
        expenses = db_helper.fetch_expenses_for_date(expense_date)
    except (mysql.connector.Error, RuntimeError) as error:
        raise HTTPException(status_code=503, detail="The database is unavailable or not configured.") from error
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database.")

    return expenses


@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses:List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)

    return {"message": "Expenses updated successfully"}


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    deleted_count = db_helper.delete_expense(expense_id)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Expense not found.")

    return {"message": "Expense deleted successfully"}


@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    try:
        data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    except (mysql.connector.Error, RuntimeError) as error:
        raise HTTPException(status_code=503, detail="The database is unavailable or not configured.") from error
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database.")

    total = sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }

    return breakdown


@app.get("/monthly_summary/")
def get_monthly_summary():
    try:
        monthly_summary = db_helper.fetch_monthly_expense_summary()
    except (mysql.connector.Error, RuntimeError) as error:
        raise HTTPException(status_code=503, detail="The database is unavailable or not configured.") from error
    if monthly_summary is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve monthly expense summary from the database.")

    return monthly_summary
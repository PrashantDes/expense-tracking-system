# Expense Tracking System

A full-stack expense management application built with Streamlit, FastAPI, MySQL, and Python.

## Features

- Add, update, and delete expenses by date
- View spending by category and date range
- View monthly spending totals
- Validate expense and date-range input
- REST API documented through FastAPI Swagger UI

## Project structure

```text
backend/       FastAPI application and database helpers
database/      MySQL schema and sample data
frontend/      Streamlit application
tests/         Automated tests
requirements.txt
```

## Setup

Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create a local `.env` file from `.env.example` and set the MySQL credentials.
Import `database/expense_db_creation.sql` into MySQL before starting the app.

## Run locally

Start the API in one terminal:

```powershell
cd backend
uvicorn server:app --reload
```

Start Streamlit from a second terminal at the project root:

```powershell
streamlit run frontend\app.py
```

Open `http://localhost:8501` for Streamlit or `http://localhost:8000/docs`
for the FastAPI documentation.

For a deployed API, set `API_URL` to the public API URL before starting Streamlit.
![Dashboard Preview](https://github.com/PrashantDes/expense-tracking-system/blob/main/ui%20snapshot.png)

## Test

Run the test suite from the project root:

```powershell
pytest
```

## Configuration

| Variable | Purpose |
| --- | --- |
| `DB_HOST` | MySQL host |
| `DB_USER` | MySQL user |
| `DB_PASSWORD` | MySQL password |
| `DB_NAME` | MySQL database name |
| `API_URL` | FastAPI URL used by Streamlit |

Never commit `.env`, passwords, logs, or the `.venv` directory.

import os
from contextlib import contextmanager
from pathlib import Path

import mysql.connector

try:
    from .logging_setup import setup_logger
except ImportError:
    from logging_setup import setup_logger


logger = setup_logger("db_helper")


def _load_local_environment():
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if not env_path.is_file():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


_load_local_environment()


@contextmanager
def get_db_cursor(commit=False):
    password = os.getenv("DB_PASSWORD")
    if password is None:
        raise RuntimeError(
            "Database credentials are not configured. Set DB_PASSWORD in the local .env file."
        )

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=password,
        database=os.getenv("DB_NAME", "expense_manager"),
    )
    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor
        if commit:
            connection.commit()
    except Exception:
        if commit:
            connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def fetch_expenses_for_date(expense_date):
    logger.info("fetch_expenses_for_date called with %s", expense_date)
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        return cursor.fetchall()


def delete_expenses_for_date(expense_date):
    logger.info("delete_expenses_for_date called with %s", expense_date)
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def delete_expense(expense_id):
    logger.info("delete_expense called with id %s", expense_id)
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
        return cursor.rowcount


def insert_expense(expense_date, amount, category, notes):
    logger.info(
        "insert_expense called with date %s, amount %s, category %s",
        expense_date,
        amount,
        category,
    )
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) "
            "VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes),
        )


def fetch_expense_summary(start_date, end_date):
    logger.info("fetch_expense_summary called with start %s end %s", start_date, end_date)
    with get_db_cursor() as cursor:
        cursor.execute(
            """SELECT category, SUM(amount) AS total
               FROM expenses
               WHERE expense_date BETWEEN %s AND %s
               GROUP BY category;""",
            (start_date, end_date),
        )
        return cursor.fetchall()


def fetch_monthly_expense_summary():
    logger.info("fetch_monthly_expense_summary called")
    with get_db_cursor() as cursor:
        cursor.execute(
            """SELECT DATE_FORMAT(expense_date, '%Y-%m') AS month,
                      SUM(amount) AS total
               FROM expenses
               GROUP BY DATE_FORMAT(expense_date, '%Y-%m')
               ORDER BY month;"""
        )
        return cursor.fetchall()

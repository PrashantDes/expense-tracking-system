import streamlit as st
from datetime import datetime
import os
import requests

API_URL = os.getenv("API_URL", "http://localhost:8000").rstrip("/")
REQUEST_TIMEOUT = 10


def add_update_tab():
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility="collapsed")
    try:
        response = requests.get(f"{API_URL}/expenses/{selected_date}", timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        existing_expenses = response.json()
    except requests.RequestException as error:
        st.error(f"Unable to load expenses: {error}")
        existing_expenses = []

    selected_date_key = str(selected_date)
    is_adding_expense = st.session_state.get("adding_expense_date") == selected_date_key

    if not existing_expenses and not is_adding_expense:
        st.info("No expenses recorded for this date.")
        if st.button("Add expense", key=f"add_expense_{selected_date_key}"):
            st.session_state["adding_expense_date"] = selected_date_key
            st.rerun()
        return

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]
    row_count = 1 if is_adding_expense and not existing_expenses else 5

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        expenses = []
        for i in range(row_count):
            if i < len(existing_expenses):
                expense_id = existing_expenses[i].get("id")
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                expense_id = None
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount,
                                               key=f"amount_{selected_date_key}_{i}",
                                               label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category", options=categories, index=categories.index(category),
                                              key=f"category_{selected_date_key}_{i}", label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="Notes", value=notes, key=f"notes_{selected_date_key}_{i}",
                                            label_visibility="collapsed")

            expenses.append({
                'id': expense_id,
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

        submit_button = st.form_submit_button()
        if submit_button:
            try:
                filtered_expenses = [
                    {key: value for key, value in expense.items() if key != "id"}
                    for expense in expenses if expense['amount'] > 0
                ]
                response = requests.post(
                    f"{API_URL}/expenses/{selected_date}",
                    json=filtered_expenses,
                    timeout=REQUEST_TIMEOUT,
                )
                response.raise_for_status()
                st.success("Expenses updated successfully!")
                st.session_state["adding_expense_date"] = None
                st.rerun()
            except requests.RequestException as error:
                st.error(f"Unable to save expenses: {error}")

    if existing_expenses:
        st.subheader("Delete an expense")
        expense_to_delete = st.selectbox(
            "Select expense",
            existing_expenses,
            format_func=lambda expense: (
                f"{expense['category']} - {expense['amount']:.2f} ({expense['notes']})"
            ),
            key=f"delete_expense_{selected_date_key}",
        )
        if st.button("Delete selected expense", key=f"delete_button_{selected_date_key}"):
            try:
                response = requests.delete(
                    f"{API_URL}/expenses/{expense_to_delete['id']}",
                    timeout=REQUEST_TIMEOUT,
                )
                response.raise_for_status()
                st.success("Expense deleted successfully!")
                st.rerun()
            except requests.RequestException as error:
                st.error(f"Unable to delete expense: {error}")
import streamlit as st
from datetime import datetime
import os
import requests
import pandas as pd


API_URL = os.getenv("API_URL", "http://localhost:8000").rstrip("/")
REQUEST_TIMEOUT = 10


def analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))

    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        try:
            response = requests.post(
                f"{API_URL}/analytics/",
                json=payload,
                timeout=REQUEST_TIMEOUT,
            )
            response.raise_for_status()
            response_data = response.json()
        except requests.RequestException as error:
            st.error(f"Unable to load analytics: {error}")
            return

        data = {
            "Category": list(response_data.keys()),
            "Total": [response_data[category]["total"] for category in response_data],
            "Percentage": [response_data[category]["percentage"] for category in response_data],
        }

        if not data["Category"]:
            st.info("No expense data is available for this date range.")
            return

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)

        st.title("Expense Breakdown By Category")

        st.bar_chart(data=df_sorted.set_index("Category")['Percentage'])
        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

        st.table(df_sorted)

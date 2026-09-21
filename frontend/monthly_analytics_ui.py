import pandas as pd
import requests
import streamlit as st
import os


API_URL = os.getenv("API_URL", "http://localhost:8000").rstrip("/")
REQUEST_TIMEOUT = 10


def monthly_analytics_tab():
    st.subheader("Monthly Expense Summary")

    if st.button("Load monthly analytics", key="load_monthly_analytics"):
        try:
            response = requests.get(f"{API_URL}/monthly_summary/", timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            monthly_summary = response.json()
        except requests.RequestException as error:
            st.error(f"Unable to load monthly analytics: {error}")
            return

        if not monthly_summary:
            st.info("No expense data is available for monthly analysis.")
            return

        data = pd.DataFrame(monthly_summary)
        data["month"] = pd.to_datetime(data["month"]).dt.strftime("%B %Y")
        data["total"] = data["total"].astype(float)

        st.bar_chart(data=data.set_index("month")["total"])
        st.dataframe(
            data.rename(columns={"month": "Month", "total": "Total"}),
            hide_index=True,
            use_container_width=True,
            column_config={"Total": st.column_config.NumberColumn(format="%.2f")},
        )

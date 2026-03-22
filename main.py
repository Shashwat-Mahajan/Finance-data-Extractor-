import streamlit as st
import re
import json
import pandas as pd
from data_extractor import extract


# ----------------------------
# Extract Function
# ----------------------------



# ----------------------------
# Streamlit UI
# ----------------------------
st.title("📊 Financial Data Extractor")

text = st.text_area("Enter financial paragraph:")

if st.button("Extract"):
    if text:
        extracted_data = extract(text)

        # 🔹 JSON Output
        st.subheader("🧾 JSON Output")
        st.code(json.dumps(extracted_data, indent=2), language="json")

        # 🔹 Table Output
        st.subheader("📈 Extracted Table")

        df = pd.DataFrame({
            "Metric": ["Revenue", "EPS"],
            "Estimated": [extracted_data["revenue_expected"], extracted_data["eps_expected"]],
            "Actual": [extracted_data["revenue_actual"], extracted_data["eps_actual"]]
        })

        st.table(df)

    else:
        st.warning("Please enter a paragraph to extract data from.")

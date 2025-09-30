# pylint: disable=missing-module-docstring
import io

import duckdb as db
import pandas as pd
import streamlit as st

st.write(
    """# SQL SRS
    Spaced Repetition System SQL practice"""
)

CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""

beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""

food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_items
"""
solution = db.query(ANSWER_STR)

with st.sidebar:
    option = st.selectbox(
        "What would you like to review",
        ["Join", "Groupby", "Windows Functions"],
        index=None,
        placeholder="Select a theme ...",
    )
    st.write(f"You selected : {option}")

st.header("enter your code")
query = st.text_area(label="Votre code SQL ici", key="user_input")
if query:
    result = db.query(query)
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table : beverages")
    st.dataframe(beverages)
    st.write("table : food_items")
    st.dataframe(food_items)
    st.write("expected : ")
    st.dataframe(solution)

with tab3:
    st.write(ANSWER_STR)

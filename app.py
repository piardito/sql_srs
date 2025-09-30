# pylint: disable=missing-module-docstring
import io

import duckdb as db
import pandas as pd
import streamlit as st

st.write(
    """# SQL SRS
    Spaced Repetition System SQL practice"""
)


ANSWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

con = db.connect(database="data/exercises_sql_tables.duckdb", read_only=False)
#solution_df = db.query(ANSWER_STR).df()

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review",
        ("cross_joins", "Groupby", "Windows Functions"),
        index=None,
        placeholder="Select a theme ...",
    )
    st.write(f"You selected : {theme}")
    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)


st.header("enter your code")
query = st.text_area(label="Votre code SQL ici", key="user_input")
# if query:
#     result = db.query(query).df()
#     st.dataframe(result)
#
#     if len(result.columns) != len(solution_df.columns):
#         st.write("Some colums are missing")
#     try:
#         result = result[solution_df.columns]
#         st.dataframe(result.compare(solution_df))
#     except KeyError as e:
#         st.write("some columns are missing")
#
#     n_lines_differences = result.shape[0] - solution_df.shape[0]
#     if n_lines_differences != 0:
#         st.write(
#             f"result has a {n_lines_differences} lines differences with the solution"
#         )
#
#
# tab2, tab3 = st.tabs(["Tables", "Solution"])
#
# with tab2:
#     st.write("table : beverages")
#     st.dataframe(beverages)
#     st.write("table : food_items")
#     st.dataframe(food_items)
#     st.write("expected : ")
#     st.dataframe(solution_df)

# with tab3:
#     st.write(ANSWER_STR)

# pylint: disable=missing-module-docstring
import io

import duckdb as db
import pandas as pd
import streamlit as st
import ast

st.write(
    """# SQL SRS
    Spaced Repetition System SQL practice"""
)



con = db.connect(database="data/exercises_sql_tables.duckdb", read_only=False)


with st.sidebar:
    theme = st.selectbox(
        "What would you like to review",
        ("cross_joins", "Groupby", "window_functions"),
        index=None,
        placeholder="Select a theme ...",
    )
    st.write(f"You selected : {theme}")
    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)

if theme is None:
        st.error("Veuillez choisir un thème dans la liste.")
        st.stop()

if exercise.empty:
        st.error("Aucun exercice trouvé pour ce thème.")
        st.stop()

st.write(exercise)

exercice_name = exercise.loc[0, "exercise_name"]
with open(f"answers/{exercice_name}.sql", "r") as f:
        answer = f.read()
solution_df = con.execute(answer).df()


st.header("enter your code")
query = st.text_area(label="Votre code SQL ici", key="user_input")
if query:
    result = con.execute(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("some columns are missing")

    n_lines_differences = result.shape[0] - solution_df.shape[0]
    if n_lines_differences != 0:
        st.write(
            f"result has a {n_lines_differences} lines differences with the solution"
        )


tab2, tab3 = st.tabs(["Tables", "Solution"])
with tab2:
      exercise_tables = ast.literal_eval(exercise.loc[0,"tables"])
      for table in exercise_tables:
          st.write(f"table : {table}")
          df_table = con.execute(f"SELECT * FROM {table}").df()
          st.dataframe(df_table)

with tab3:
    st.write(answer)

import streamlit as st
import pandas as pd
import duckdb as db
import io

st.write("""# SQL SRS
    Spaced Repetition System SQL practice""")

csv = '''
beverage,price
orange juice,2.5
Expresso,2
Tea,3
'''

beverages = pd.read_csv(io.StringIO(csv))

csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""

food_items = pd.read_csv(io.StringIO(csv2))

answer_str = """
SELECT * FROM beverages
CROSS JOIN food_items
"""
solution_df = db.query(answer_str).df()

with st.sidebar :
    option = st.selectbox(
        "What would you like to review",
        ['Join','Groupby','Windows Functions'],
        index = None,
        placeholder = "Select a theme ..."
    )
    st.write(f"You selected : {option}")

st.header("enter your code")
query = st.text_area(label = "votre code SQL ici",key = "user_input")
if query:
    result = db.query(query).df()
    st.dataframe(result)

    if len(result.columns) != len(solution_df.columns):
        st.write("Some colums are missing")
    try :
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("some columns are missing")


    n_lines_differences = result.shape[0] - solution_df.shape[0]
    if n_lines_differences !=0 :
        st.write(
            f"result has a {n_lines_differences} lines differences with the solution"
        )



tab2,tab3 = st.tabs(['Tables','Solution'])

with tab2:
    st.write("table : beverages")
    st.dataframe(beverages)
    st.write("table : food_items")
    st.dataframe(food_items)
    st.write("expected : ")
    st.dataframe(solution_df)

with tab3 :
    st.write(answer_str)



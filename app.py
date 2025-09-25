import streamlit as st
import pandas as pd
import duckdb as db

st.write('Hello world')
data = {"a": [1,2,3],"b":[4,5,6]}
df = pd.DataFrame(data)


tab1,tab2,tab3 = st.tabs(['Cat','Dog','Dwl'])
with tab1:
    sql_query = st.text_area(label="entrez votre input")
    q = f"""
    {sql_query}
    """
    st.dataframe(db.query(q))
    st.dataframe(df)
with tab2 :
    pass
with tab3 :
    pass

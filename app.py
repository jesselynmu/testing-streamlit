import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

db = st.secrets["database"]

conn_str = (
    f"mssql+pyodbc://{db['username']}:{db['password']}@{db['server']}/"
    f"{db['database']}?driver={db['driver'].replace(' ', '+')}"
)

engine = create_engine(conn_str)

st.title("📊 Data dari SQL Server")
df = pd.read_sql("SELECT * FROM dbo.stg_public_brand", engine)
st.dataframe(df)
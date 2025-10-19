import streamlit as st
from db_connection import get_connection
import pandas as pd

st.set_page_config(page_title="Available Books", page_icon="📚", layout="wide")
st.title("📖 Available Books")

# Fetch books
conn = get_connection()
df = pd.read_sql("SELECT book_title, author, genre, condition_status, donor_name FROM donations", conn)
conn.close()

st.dataframe(df)

import streamlit as st
from db_connection import get_connection
import pandas as pd

st.set_page_config(page_title="Donors List", page_icon="🧑‍🤝‍🧑", layout="wide")
st.title("📋 Donors List")

# Fetch donors
conn = get_connection()
df = pd.read_sql("SELECT donor_name, email, phone, donor_type FROM donations", conn)
conn.close()

st.dataframe(df)

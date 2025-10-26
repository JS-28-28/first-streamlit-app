import streamlit as st
from db_connection import get_connection
import pandas as pd

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")

col1, col2, col3 = st.columns([6,1,1])
with col3:
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.success("Logged out successfully ✅")
        st.switch_page("pages/login.py")

if 'user' not in st.session_state:
    st.warning("Please login to access this page.")
    st.stop()

st.set_page_config(page_title="Donors List", page_icon="🧑‍🤝‍🧑", layout="wide")
st.title("📋 Donors List")

conn = get_connection()
df = pd.read_sql("SELECT donor_name, email, phone, donor_type FROM donations", conn)
conn.close()

st.dataframe(df)


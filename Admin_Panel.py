import streamlit as st
from db_connection import get_connection
import pandas as pd

st.set_page_config(page_title="Admin Panel", page_icon="🛠️", layout="wide")
st.title("🛠️ Admin Panel")

# Admin login simple check
password = st.text_input("Enter Admin Password", type="password")
if password == "admin123":  # simple password
    conn = get_connection()
    df_users = pd.read_sql("SELECT * FROM users", conn)
    df_books = pd.read_sql("SELECT * FROM donations", conn)
    conn.close()

    st.subheader("All Users")
    st.dataframe(df_users)

    st.subheader("All Donations / Books")
    st.dataframe(df_books)

    # Optionally, delete a record
    st.subheader("Delete Donation")
    del_id = st.number_input("Enter Donation ID to Delete", min_value=1, step=1)
    if st.button("Delete"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM donations WHERE id=%s", (del_id,))
        conn.commit()
        conn.close()
        st.success(f"Donation ID {del_id} deleted successfully!")
else:
    st.warning("Enter correct admin password to access the panel.")

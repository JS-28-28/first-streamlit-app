import streamlit as st
from db_connection import get_connection
import pandas as pd

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")

st.set_page_config(page_title="Admin Panel", page_icon="🛠️", layout="wide")
st.title("🛠️ Admin Panel")

password = st.text_input("Enter Admin Password", type="password")
if password == "admin123":
    conn = get_connection()
    df_users = pd.read_sql("SELECT * FROM users", conn)
    df_books = pd.read_sql("SELECT * FROM donations", conn)

    query_requests = """
    SELECT r.id, r.username, d.book_title, d.author, r.request_date
    FROM requests r
    JOIN donations d ON r.book_id = d.id
    ORDER BY r.request_date DESC
    """
    df_requests = pd.read_sql(query_requests, conn)
    conn.close()

    st.subheader("All Users")
    st.dataframe(df_users)

    st.subheader("All Donations / Books")
    st.dataframe(df_books)

    st.subheader("Requested Books")
    if df_requests.empty:
        st.info("No book requests found.")
    else:
        st.dataframe(df_requests)

    st.subheader("Delete Donation")
    del_id = st.number_input("Enter Donation ID to Delete", min_value=1, step=1)
    if st.button("Delete"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM donations WHERE id=?", (del_id,))
            conn.commit()
            conn.close()
            st.success(f"Donation ID {del_id} deleted successfully!")
        except Exception as e:
            st.error(f"Database Error: {e}")
else:
    st.warning("Enter correct admin password to access the panel.")


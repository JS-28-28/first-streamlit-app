import streamlit as st
from db_connection import get_connection
import pandas as pd

# Apply common CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Logout button (top-right corner)
col1, col2, col3 = st.columns([6, 1, 1])
with col3:
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.success("Logged out successfully ✅")
        st.switch_page("pages/login.py")

# Check login
if 'user' not in st.session_state:
    st.warning("Please login to access this page.")
    st.stop()

st.set_page_config(page_title="Available Books", page_icon="📚", layout="wide")
st.title("📖 Available Books")

# Fetch books from DB
conn = get_connection()
df = pd.read_sql("SELECT id, book_title, author, genre, condition_status, donor_name FROM donations", conn)
conn.close()

# Show books with checkboxes
selected_books = []
for idx, row in df.iterrows():
    checkbox_label = f"{row['book_title']} by {row['author']} | Genre: {row['genre']} | Condition: {row['condition_status']} | Donor: {row['donor_name']}"
    if st.checkbox(checkbox_label, key=f"book_{row['id']}"):
        selected_books.append(row['id'])

# Request button
if st.button("Request Selected Books"):
    if selected_books:
        # Save request in DB (example: insert into requests table)
        conn = get_connection()
        cursor = conn.cursor()
        for book_id in selected_books:
            cursor.execute(
                "INSERT INTO requests (username, book_id) VALUES (%s, %s)",
                (st.session_state['user']['username'], book_id)
            )
        conn.commit()
        conn.close()
        st.success(f"Requested {len(selected_books)} book(s) successfully!")
    else:
        st.warning("Please select at least one book to request.")

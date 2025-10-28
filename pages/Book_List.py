import streamlit as st
from db_connection import get_connection
import pandas as pd

# ---------- Load custom CSS ----------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")

# ---------- Logout Button ----------
col1, col2, col3 = st.columns([6, 1, 1])
with col3:
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.success("Logged out successfully ✅")
        st.switch_page("pages/login.py")

# ---------- Authentication Check ----------
if 'user' not in st.session_state:
    st.warning("Please login to access this page.")
    st.stop()

# ---------- Page Setup ----------
st.set_page_config(page_title="Available Books", page_icon="📚", layout="wide")
st.title("📖 Available Books")

# ---------- Fetch Data ----------
conn = get_connection()
# Include book_pdf column so we can show links
df = pd.read_sql("""
    SELECT id, book_title, author, genre, condition_status, donor_name, book_pdf
    FROM donations
""", conn)
conn.close()

# ---------- Book List Display ----------
selected_books = []
for idx, row in df.iterrows():
    checkbox_label = (
        f"{row['book_title']} by {row['author']} | "
        f"Genre: {row['genre']} | "
        f"Condition: {row['condition_status']} | "
        f"Donor: {row['donor_name']}"
    )
    if st.checkbox(checkbox_label, key=f"book_{row['id']}"):
        selected_books.append(row['id'])
    
    # ✅ Display link to view or download the PDF
    if row['book_pdf']:
        st.markdown(
            f"[📘 View or Download PDF]({row['book_pdf']})",
            unsafe_allow_html=True
        )

# ---------- Book Request Logic ----------
if st.button("Request Selected Books"):
    if selected_books:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            for book_id in selected_books:
                cursor.execute(
                    "INSERT INTO requests (username, book_id, request_date) VALUES (?,?,datetime('now'))",
                    (st.session_state['user']['username'], book_id)
                )
            conn.commit()
            conn.close()
            st.success(f"Requested {len(selected_books)} book(s) successfully! ✅")
        except Exception as e:
            st.error(f"Database Error: {e}")
    else:
        st.warning("Please select at least one book to request.")



import streamlit as st
import mysql.connector
from datetime import date

# ---------- Database Connection ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",   # your MySQL password
        database="book"
    )

# ---------- Streamlit Page Setup ----------
st.set_page_config(page_title="Book Bank Donation", layout="centered")
st.title("📚 Book Bank Donation Portal")

st.write("### Donate your books and help others learn!")

# ---------- Form Inputs ----------
with st.form("donation_form"):
    st.subheader("Donor Information")
    donor_name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    donor_type = st.selectbox("Donor Type", ["Student", "Faculty", "Businessman", "Other"])

    st.subheader("Book Information")
    book_title = st.text_input("Book Title")
    author = st.text_input("Author Name")
    genre = st.text_input("Genre / Subject")
    condition_status = st.selectbox("Book Condition", ["New", "Used - Good", "Used - Average"])
    donation_date = st.date_input("Donation Date", value=date.today())

    submitted = st.form_submit_button("📤 Submit Donation")

# ---------- Insert Data ----------
if submitted:
    if donor_name and book_title:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO donations
                (donor_name, email, phone, donor_type, book_title, author, genre, condition_status, donation_date)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            values = (donor_name, email, phone, donor_type, book_title, author, genre, condition_status, donation_date)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
            st.success("✅ Donation submitted successfully!")
        except Exception as e:
            st.error(f"Database Error: {e}")
    else:
        st.warning("Please fill in at least Donor Name and Book Title.")

import streamlit as st
import mysql.connector
from datetime import date

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


if 'user' not in st.session_state:
    st.warning("Please login to access this page.")
    st.stop()




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

# Add portal logo
#st.image("portal_logo.png", width=200)  # place your logo image in the same folder
st.title("📚 Book Donation Portal")
st.write("### Donate your books and help others learn!")


# ---------- Form Inputs ----------
with st.form("donation_form"):
    st.subheader("Donor Information")
    donor_name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    donor_type = st.selectbox("Donor Type", ["Student", "Faculty", "Businessman", "Other"])
    
    st.subheader("Books Information")
    
    # Multiple books donation
    num_books = st.number_input("How many books do you want to donate?", min_value=1, max_value=10, value=1, step=1)
    
    books = []
    for i in range(num_books):
        st.markdown(f"**Book {i+1} Details**")
        book_title = st.text_input(f"Book Title {i+1}", key=f"title_{i}")
        author = st.text_input(f"Author Name {i+1}", key=f"author_{i}")
        genre = st.text_input(f"Genre / Subject {i+1}", key=f"genre_{i}")
        condition_status = st.selectbox(f"Book Condition {i+1}", ["New", "Used - Good", "Used - Average"], key=f"condition_{i}")
        book_image = st.file_uploader(f"Upload Image of Book {i+1}", type=["png","jpg","jpeg"], key=f"image_{i}")
        books.append((book_title, author, genre, condition_status, book_image))
    
    donation_date = st.date_input("Donation Date", value=date.today())
    submitted = st.form_submit_button("📤 Submit Donation")

# ---------- Insert Data ----------
if submitted:
    if donor_name and all([b[0] for b in books]):  # ensure donor name & at least book titles filled
        try:
            conn = get_connection()
            cursor = conn.cursor()
            for book in books:
                book_title, author, genre, condition_status, book_image = book
                
                # Save book image to 'book_images' folder
                img_path = None
                if book_image:
                    img_path = f"book_images/{book_image.name}"
                    with open(img_path, "wb") as f:
                        f.write(book_image.getbuffer())
                
                query = """
                    INSERT INTO donations
                    (donor_name, email, phone, donor_type, book_title, author, genre, condition_status, donation_date, book_image)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
                values = (donor_name, email, phone, donor_type, book_title, author, genre, condition_status, donation_date, img_path)
                cursor.execute(query, values)
            
            conn.commit()
            conn.close()
            st.success("✅ Donation submitted successfully!")
        except Exception as e:
            st.error(f"Database Error: {e}")
    else:
        st.warning("Please fill in at least Donor Name and all Book Titles.")

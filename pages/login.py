import streamlit as st
from db_connection import get_connection
import hashlib

# Apply common CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# --- PAGE CONFIG ---
st.set_page_config(page_title="Login / Signup", page_icon="🔑", layout="centered")

# --- Hash password ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- Login Function ---
def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password, user_type FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and result[0] == hash_password(password):
        return True, result[1].strip().lower()
    return False, None

# --- Signup Function ---
def signup_user(username, email, password, user_type):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password, user_type) VALUES (?, ?, ?, ?)",
            (username, email, hash_password(password), user_type.strip().lower())
        )
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False

# --- Tabs ---
tab1, tab2 = st.tabs(["Login", "Signup"])

# ------------------- LOGIN TAB -------------------
with tab1:
    st.subheader("Login")
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")
    
    if st.button("Login"):
        success, user_type = login_user(username, password)
        if success:
            st.session_state['user'] = {
                'username': username,
                'role': user_type
            }
            st.success(f"Login Successful! Welcome {username} ({user_type})")

            # Redirect or show navigation
            if user_type == 'admin':
                st.switch_page("pages/Admin_Panel.py")
            elif user_type in ['student', 'faculty', 'donor', 'other']:
                st.info("Choose an option below:")
                st.page_link("pages/Book_List.py", label="📚 View Available Books")
                st.page_link("pages/book_bank_app.py", label="📤 Donate a Book")
            else:
                st.warning(f"Unknown user type: '{user_type}'. Cannot redirect.")
        else:
            st.error("Incorrect username or password.")

# ------------------- SIGNUP TAB -------------------
with tab2:
    st.subheader("Signup")
    new_username = st.text_input("Username", key="signup_user")
    new_email = st.text_input("Email", key="signup_email")
    new_password = st.text_input("Password", type="password", key="signup_pass")

    role_map = {
        "Student": "student",
        "Faculty": "faculty",
        "Other": "other",
        "Admin": "admin"
    }
    role_label = st.selectbox("User Type", list(role_map.keys()))
    user_type = role_map[role_label]

    if st.button("Signup"):
        if signup_user(new_username, new_email, new_password, user_type):
            st.success("Signup successful! Please login.")
        else:
            st.error("Username or Email already exists.")



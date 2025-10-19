import streamlit as st
from db_connection import get_connection
import hashlib

# --- PAGE CONFIG ---
st.set_page_config(page_title="Login / Signup", page_icon="🔑", layout="centered")

# --- Hash password ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- Login Function ---
def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password, user_type FROM users WHERE username=%s", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and result[0] == hash_password(password):
        return True, result[1]
    return False, None

# --- Signup Function ---
def signup_user(username, email, password, user_type):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password, user_type) VALUES (%s,%s,%s,%s)",
            (username, email, hash_password(password), user_type)
        )
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False

# --- Tabs ---
tab1, tab2 = st.tabs(["Login", "Signup"])

#------------- LOGIN TAB----------------------
with tab1:
    st.subheader("Login")
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password",  key="login_pass")
    if st.button("Login"):
        success, user_type = login_user(username, password)
        if success:
            st.success(f"Login Successful! Welcome {username} ({user_type})")
        else:
            st.error("Incorrect username or password")

#------------------------ SIGNUP TAB ---------------------
with tab2:
    st.subheader("Signup")
    new_username = st.text_input("Username", key="signup_user")
    new_email = st.text_input("Email", key="signup_email")
    new_password = st.text_input("Password", type="password", key="signup_pass")
    user_type = st.selectbox("User Type", ["student","faculty","other"])
    if st.button("Signup"):
        if signup_user(new_username, new_email, new_password, user_type):
            st.success("Signup successful! Please login.")
        else:
            st.error("Username or Email already exists.")

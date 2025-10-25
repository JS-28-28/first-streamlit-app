import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Book Bank | Home", page_icon="📚", layout="wide")

# --- APPLY CUSTOM CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# --- Make sidebar toggle always visible and themed ---
st.markdown("""
    <style>
    /* Hide black header background */
    [data-testid="stHeader"] {
        background: none;
        height: 0px;
    }

    /* Keep and style the sidebar toggle button (» icon) */
    [data-testid="stToolbar"] button {
        visibility: visible !important;
        opacity: 1 !important;
        background-color: #1e3cfc !important; /* Blue shade similar to your theme */
        color: white !important;
        border: none !important;
        border-radius: 4px;
        padding: 0.25rem 0.6rem;
        transition: 0.2s ease-in-out;
    }

    /* Optional hover effect */
    [data-testid="stToolbar"] button:hover {
        background-color: #315efb !important;
        transform: scale(1.05);
    }

    /* Adjust position if needed */
    [data-testid="stToolbar"] {
        right: 1rem;
        top: 0.5rem;
        display: flex !important;
        align-items: center;
    }

    /* Keep nice spacing at top of page */
    [data-testid="stAppViewContainer"] {
        padding-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- (Removed Sidebar Section) ---
# The previous sidebar navigation is now deleted to clean up the UI

# --- NAVBAR ---

# --- MAIN CONTENT ---
st.markdown("<h1 class='main-title'>📚 Welcome to the Book Bank</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>A platform to donate, share, and spread knowledge freely.</p>", unsafe_allow_html=True)

# --- ABOUT SECTION ---
st.markdown("""
<div class='about-section'>
<h3>💡 Our Motive</h3>
<p>
The <span class='highlight'>Book Bank</span> connects book donors and learners.
Many students or individuals have valuable books that remain unused after some time, while others search for the same books but can't afford them.
</p>
<p>
Through this platform, donors can easily list the books they wish to donate and students can access them for <span class='highlight'>free</span>.
Our goal is to encourage sharing, sustainability, and equal learning opportunities for everyone.
</p>

<h3>🌟 Key Features</h3>
<ul>
<li>Free Book Donations and Listings</li>
<li>Transparent Donor Details</li>
<li>Simple Login & Signup System</li>
<li>Admin Control for Database Management</li>
</ul>
</div>
""", unsafe_allow_html=True)

# --- CALL TO ACTION ---
# --- CALL TO ACTION (Centered Get Started Button) ---
st.markdown("<div class='get-started-container'>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🚀 Get Started", key="get_started_btn"):
        st.switch_page("pages/login.py")
st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<div class='footer'>© Book Bank Project | Developed by JS</div>", unsafe_allow_html=True)

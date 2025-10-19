import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Book Bank | Home",
    page_icon="📚",
    layout="wide",
)

# --- CUSTOM CSS FOR BEAUTY ---
st.markdown("""
    <style>
        body {
            background-color: #f9fafc;
        }
        .main-title {
            text-align: center;
            color: #1E3A8A;
            font-size: 45px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .sub-title {
            text-align: center;
            font-size: 20px;
            color: #334155;
        }
        .about-section {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
        .highlight {
            color: #2563EB;
            font-weight: 600;
        }
        .cta-button {
            text-align: center;
            margin-top: 30px;
        }
        .footer {
            text-align: center;
            color: #64748b;
            font-size: 14px;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown("<h1 class='main-title'>📚 Welcome to the Book Bank</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>A platform to donate, share, and spread knowledge freely.</p>", unsafe_allow_html=True)

# --- ABOUT SECTION ---
st.markdown("""
<div class='about-section'>
    <h3>💡 Our Motive</h3>
    <p>
        The <span class='highlight'>Book Bank</span> is an initiative that connects book donors and learners.  
        Many students or individuals have valuable books that remain unused after some time — while others search for the same books but can’t afford them.
    </p>
    <p>
        Through this platform, donors can easily list the books they wish to donate, 
        and students can access them for <span class='highlight'>free</span>.  
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

# --- CALL TO ACTION BUTTON ---
st.markdown("<div class='cta-button'>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Get Started"):
        st.switch_page("pages/login.py")
st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<div class='footer'>©  Book Bank Project | Developed by Jharna Sahu</div>", unsafe_allow_html=True)

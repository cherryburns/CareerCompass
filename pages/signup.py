import streamlit as st
import json
import os
import re

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="CareerCompass - Sign Up",
    page_icon="📝",
    layout="centered"
)

# --------------------------------------------------
# USER FILE
# --------------------------------------------------

USER_FILE = "users.json"


# --------------------------------------------------
# LOAD USERS
# --------------------------------------------------

def load_users():
    if not os.path.exists(USER_FILE):
        return {}

    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except:
        return {}


# --------------------------------------------------
# SAVE USERS
# --------------------------------------------------

def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #8B4CF5 0%,
        #B957C9 50%,
        #FF8A4C 100%
    );
}

.block-container {
    max-width: 600px;
    padding-top: 40px;
}

.signup-box {
    background: white;
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.20);
}

.signup-title {
    text-align: center;
    color: #2E005D;
    font-size: 32px;
    font-weight: 700;
}

.signup-subtitle {
    text-align: center;
    color: #666666;
    margin-bottom: 25px;
}

div.stButton > button {
    width: 100%;
    border-radius: 10px;
    border: none;
    background: linear-gradient(
        90deg,
        #8B4CF5,
        #B957C9,
        #FF8A4C
    );
    color: white;
    font-size: 16px;
    font-weight: 600;
    padding: 10px;
}

div.stButton > button:hover {
    color: white;
    transform: translateY(-2px);
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown(
    '<div class="signup-title">Create Your Account</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="signup-subtitle">'
    'Join CareerCompass and start your career journey.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIGN UP FORM
# --------------------------------------------------

username = st.text_input(
    "👤 Username",
    placeholder="Enter your username"
)

phone = st.text_input(
    "📱 Phone Number",
    placeholder="Enter 10-digit phone number"
)

password = st.text_input(
    "🔐 Password",
    type="password",
    placeholder="Enter exactly 8 characters"
)

confirm_password = st.text_input(
    "🔐 Confirm Password",
    type="password",
    placeholder="Re-enter your password"
)


# --------------------------------------------------
# PASSWORD INFORMATION
# --------------------------------------------------

st.caption("Password must contain exactly 8 characters.")


# --------------------------------------------------
# CREATE ACCOUNT
# --------------------------------------------------

if st.button("Create Account"):

    # Check empty fields
    if not username or not phone or not password or not confirm_password:

        st.error("Please fill in all fields.")

    # Username validation
    elif len(username.strip()) < 3:

        st.error("Username must contain at least 3 characters.")

    # Phone validation
    elif not re.fullmatch(r"\d{10}", phone):

        st.error("Phone number must contain exactly 10 digits.")

    # Password length
    elif len(password) != 8:

        st.error("Password must contain exactly 8 characters.")

    # Password match
    elif password != confirm_password:

        st.error("Passwords do not match.")

    else:

        users = load_users()

        # Check if phone already exists
        if phone in users:

            st.error(
                "An account with this phone number already exists."
            )

        else:

            # Save user
            users[phone] = {
                "username": username.strip(),
                "phone": phone,
                "password": password
            }

            save_users(users)

            st.success(
                "Account created successfully! 🎉"
            )

            st.info(
                "You can now login using your phone number and password."
            )

            # Go to Login button
            if st.button("Go to Login"):

                st.switch_page("pages/login.py")


# --------------------------------------------------
# LOGIN LINK
# --------------------------------------------------

st.divider()

st.write(
    "Already have an account?"
)

if st.button("Login Here"):

    st.switch_page("login.py")
import re
import streamlit as st
import random
import string

# Page styling
st.set_page_config(page_title="🔐 Password Strength Meter", page_icon="🔐", layout="centered")

# Apply background with pink gradient contrast
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #ff9a9e, #fad0c4);
        font-family: Arial, sans-serif;
    }
    .stTextInput>div>div>input {
        border: 2px solid #FF4081;
        border-radius: 10px;
        padding: 10px;
        background-color: #fff0f5;
    }
    .stButton>button {
        background-color: #FF4081;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px 20px;
        transition: 0.3s;
        border: none;
    }
    .stButton>button:hover {
        background-color: #E91E63;
    }
    .st-expander {
        background-color: #ff80ab;
        border-radius: 10px;
    }
    .strength-bar {
        width: 100%;
        height: 10px;
        border-radius: 5px;
        margin-top: 10px;
    }
    .weak { background-color: #FF0000; }
    .moderate { background-color: #FFA500; }
    .strong { background-color: #4CAF50; }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and description
st.title("🔐 Password Strength Meter")
st.markdown("<h4 style='text-align: center; color: #FF4081;'>Ensure your password is strong and secure! 🔍</h4>", unsafe_allow_html=True)

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")
    
    if re.search(r"[!@#$%&^*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%&^*)**.")
    
    # Display password strength result
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure and strong!")
        strength_color = "strong"
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
        strength_color = "moderate"
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")
        strength_color = "weak"

    # Password Strength Bar
    st.markdown(f"<div class='strength-bar {strength_color}'></div>", unsafe_allow_html=True)
    
    # Feedback section
    if feedback:
        with st.expander("🔍 **Improve Your Password**"):
            for item in feedback:
                st.write(f"- {item}")

# Function to generate a random strong password
def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%&^*"
    return ''.join(random.choice(characters) for i in range(12))

# Password input field
col1, col2 = st.columns([4, 1])
with col1:
    password = st.text_input("Enter your password:", type="password", help="Use a mix of uppercase, lowercase, numbers, and symbols.")

with col2:
    if st.button("🔄 Generate"):
        password = generate_password()
        st.text_input("Generated Password:", password, type="password", disabled=True)

# Button to check password strength
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
        

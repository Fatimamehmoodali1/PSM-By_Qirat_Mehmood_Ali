import re
import streamlit as st
import random
import string

# Page styling
st.set_page_config(page_title="🔐 Password Strength Meter By Qirat Mehmood Ali", page_icon="🔐", layout="centered")

# Custom CSS for better styling with background fix
st.markdown("""
    <style>
        /* Apply a gradient background */
        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(to right, #ff9a9e, #fad0c4);
        }
        .main {text-align: center;}
        .stTextInput>div>div>input {border: 2px solid #4CAF50; border-radius: 10px; padding: 10px; width: 80%;}
        .stButton>button {background-color: #4CAF50; color: white; font-size: 18px; border-radius: 8px; padding: 10px 20px; width: 80%;}
        .stButton>button:hover {background-color: #45a049;}
        .st-expander {background-color: #ffcc00; border-radius: 10px;}
        .strength-bar {height: 10px; border-radius: 5px; margin-top: 10px;}
    </style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Checker")
st.markdown("<h4 style='text-align: center; color: #4CAF50;'>Ensure your password is strong and secure! 🔍</h4>", unsafe_allow_html=True)

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
        bar_color = "green"
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
        bar_color = "orange"
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")
        bar_color = "red"
    
    # Password strength meter
    st.markdown(f'<div class="strength-bar" style="width:{score * 25}%; background-color:{bar_color};"></div>', unsafe_allow_html=True)
    
    # Feedback section
    if feedback:
        with st.expander("🔍 **Improve Your Password**"):
            for item in feedback:
                st.write(f"- {item}")

# Function to generate a random password
def generate_password(length=12, use_specials=True):
    characters = string.ascii_letters + string.digits
    if use_specials:
        characters += "!@#$%&^*"
    return ''.join(random.choice(characters) for _ in range(length))

# Password input field
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")

# Button to check password strength
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")

# Random password generator
st.markdown("### Generate a Strong Password 🔄")
password_length = st.slider("Select Password Length", 8, 20, 12)
include_specials = st.checkbox("Include Special Characters (!@#$%&^*)", value=True)
if st.button("🔄 Generate Password"):
    generated_password = generate_password(password_length, include_specials)
    st.text_input("Generated Password:", generated_password, type="password", disabled=True)

import re
import streamlit as st

# Page styling
st.set_page_config(page_title="🔐 Password Strength Meter", page_icon="🔐", layout="centered")

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput > div > div > input {
        width: 60%;
        padding: 10px;
        font-size: 18px;
        border-radius: 10px;
        border: 2px solid #4CAF50;
        background-color: #f1f8f6;
    }
    .stButton button {
        width: 50%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
        border: none;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .success {
        color: #008000;
        font-weight: bold;
        font-size: 18px;
    }
    .info {
        color: #FFA500;
        font-weight: bold;
        font-size: 18px;
    }
    .error {
        color: #FF0000;
        font-weight: bold;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Checker")
st.write("### Ensure your password is secure and strong 🔍")

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
    
    # Display password strength result with colored text
    if score == 4:
        st.success("✅ **Strong Password:** Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password:** Consider adding more complexity for better security.")
    else:
        st.error("❌ **Weak Password:** Follow the suggestions below to strengthen it.")
    
    # Display feedback in an expandable section
    if feedback:
        with st.expander("🔍 **Improve Your Password**"):
            for item in feedback:
                st.write(f"<span class='error'>{item}</span>", unsafe_allow_html=True)

# Password input field with enhanced UI
password = st.text_input("Enter your password:", type="password", help="Use a mix of uppercase, lowercase, numbers, and symbols.")

# Button to check password strength
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")

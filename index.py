import re
import streamlit as st

# Page styling 
st.set_page_config(page_title="Password Strength Meter", page_icon="", layout="centered")

# Load custom CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Generator")
st.write("📝 Enter your password below to check its security level.")

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
        feedback.append("🔠 Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔢 Password should include **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("⚠️ Include **at least one special character (!@#$%^&*)**.")

    # Display password strength results
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure 🔒.")
    elif score == 3:
        st.info("🟡 **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❗ **Weak Password** - Follow the suggestions below to strengthen it.")

    # Feedback
    if feedback:
        with st.expander("💡 **Improve your password**"):
            for item in feedback:
                st.write(item)

password = st.text_input("🔑 Enter your password", type="password", help="Ensure your password is strong")

# Button
if st.button("🔍 Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
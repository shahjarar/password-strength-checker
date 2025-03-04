import re
import streamlit as st # type: ignore


def check_password_strength(password: str) -> str:
    length_criteria = len(password) >= 8
    digit_criteria = bool(re.search(r"\d", password))
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    strength_score = sum([length_criteria, digit_criteria, uppercase_criteria, lowercase_criteria, special_char_criteria])
    
    if strength_score == 5:
        return "Strong"
    elif strength_score >= 3:
        return "Medium"
    else:
        return "Weak"

st.title("🔒 Password Strength Checker")
password = st.text_input("Enter your password:", type="password")

if password:
    strength = check_password_strength(password)
    st.write(f"**Password Strength:** {strength}")



import streamlit as st

# Set up the app with page configuration
st.set_page_config(page_title="Real Estate Underwriting Tool", layout="centered")

# Title and instructions
st.title("Real Estate Underwriting Tool")

st.info("Warning: This webpage is a prototype and is still under development")

# Sidebar for navigation
st.subheader("Navigation")

# Example: Add a button to go to the Real Estate Planning page (if it exists)
if st.button("Login/Sign Up"):
    st.switch_page("pages/Login-signup.py")
if st.button("Go to Real Estate Planning"):
    st.switch_page("pages/Real_Estate_Planning.py")
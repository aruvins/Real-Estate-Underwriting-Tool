import streamlit as st
import pandas as pd
from datetime import datetime

# Import page functions
from navi.amortization_schedule import display_amortization_schedule
from navi.rent_roll import display_rent_roll
from navi.main_page import display_main_page
from navi.summary import display_summary

# Page configuration
st.set_page_config(
    page_title="Real Estate Underwriting",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables if not already present
if 'principal' not in st.session_state:
    st.session_state.principal = 500000.0
if 'start_date' not in st.session_state:
    st.session_state.start_date = datetime(2024, 9, 1)
if 'loan_term_years' not in st.session_state:
    st.session_state.loan_term_years = 30
if 'annual_interest_rate' not in st.session_state:
    st.session_state.annual_interest_rate = 0.04
if 'monthly_payment' not in st.session_state:
    st.session_state.monthly_payment = 2387.08

# Initialize session state for rent roll if not already present
if 'units' not in st.session_state or st.session_state.units.empty:
    # Start with a default row
    st.session_state.units = pd.DataFrame([{'Unit Type': 'New Unit', 'Rent Price': 0.0, 'Number of Units': 0}])

# Custom navigation
st.title("Navigation")
page = st.selectbox("Choose a page", ["Main Page", "Summary", "Amortization Schedule", "Rent Roll" ], key="page_selector")

# Display the selected page
if page == "Main Page":
    display_main_page()
elif page == "Amortization Schedule":
    display_amortization_schedule()
elif page == "Rent Roll":
    display_rent_roll()
elif page == "Summary":
    display_summary()

import streamlit as st
import pandas as pd
from datetime import datetime

from Calculators.RentRoll import RentRoll
# Import page functions
from navi.amortization_schedule import display_amortization_schedule
from navi.rent_roll import display_rent_roll
from navi.main_page import display_main_page
from navi.summary import display_summary
from navi.proforma_month import display_proforma_month

# Page configuration
st.set_page_config(
    page_title="Real Estate Underwriting",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables if not already present
if 'principal' not in st.session_state:
    st.session_state.principal = 0.0
if 'start_date' not in st.session_state:
    st.session_state.start_date = datetime.today()
if 'loan_term_years' not in st.session_state:
    st.session_state.loan_term_years = 0
if 'annual_interest_rate' not in st.session_state:
    st.session_state.annual_interest_rate = 0.00
if 'monthly_payment' not in st.session_state:
    st.session_state.monthly_payment = 0.0
if 'total_rent' not in st.session_state:
    st.session_state.total_rent = 0.0


# Initialize session state for rent roll if not already present
if 'units' not in st.session_state or st.session_state.units.empty:
    # Start with a default row
    st.session_state.units = pd.DataFrame([{'Unit Type': 'New Unit', 'Rent Price': 0.0, 'Number of Units': 0}])

# Custom navigation
st.title("Navigation")
page = st.selectbox("Choose a page", ["Main Page", "Summary", "Pro-Forma Month", "Amortization Schedule", "Rent Roll" ], key="page_selector")

# Display the selected page
if page == "Main Page":
    display_main_page()
elif page == "Summary":
    display_summary()
elif page == "Pro-Forma Month":
    display_proforma_month()
elif page == "Amortization Schedule":
    display_amortization_schedule()
elif page == "Rent Roll":
    display_rent_roll()


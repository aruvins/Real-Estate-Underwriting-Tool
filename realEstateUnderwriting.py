import streamlit as st
import pandas as pd
from datetime import datetime

from Calculators.RentRoll import RentRoll
from Calculators.Project import Project

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
if 'project' not in st.session_state:
        st.session_state.project = Project()

def initialize_session_state():
    default_values = {
        'total_rent': 0.00,
        'parking_revenue': 0.00,
        'laundry_revenue': 0.00,
        'other_revenue': 0.00,
        'vacancy_loss': 0.00,
        'repairs_maintenance': 0.00,
        'office_expenses': 0.00,
        'management': 0.00,
        'payroll': 0.00,
        'insurance': 0.00,
        'r_and_m_account': 0.00,
        'property_tax': 0.00,
        'electricity': 0.00,
        'water_sewer': 0.00,
        'trash_disposal': 0.00,
        'misc': 0.00
    }
    for key, value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = value

# Call this function at the start
initialize_session_state()

# Initialize session state for rent roll if not already present
if 'units' not in st.session_state or st.session_state.units.empty:
    # Start with a default row
    st.session_state.units = pd.DataFrame([{'Unit Type': 'New Unit', 'Rent Price': 0.00, 'Number of Units': 0}])

# Custom navigation
st.title("Navigation")
page = st.selectbox("Choose a page", ["Main Page", "Quick Start", "Pro-Forma Month", "Amortization Schedule", "Rent Roll" ], key="page_selector")

# Display the selected page
if page == "Main Page":
    display_main_page()
elif page == "Quick Start":
    display_summary()
elif page == "Pro-Forma Month":
    display_proforma_month()
elif page == "Amortization Schedule":
    display_amortization_schedule()
elif page == "Rent Roll":
    display_rent_roll()


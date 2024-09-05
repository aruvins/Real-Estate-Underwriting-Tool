# main.py

import streamlit as st
from navi.amortization_schedule import display_amortization_schedule
from navi.rent_roll import display_rent_roll
from navi.main_page import display_main_page
from navi.summary import display_summary
from navi.proforma_month import display_proforma_month

# Check if a project is loaded
if "selected_project" not in st.session_state:
    st.warning("No project selected! Please go to the [Project Selection page](./Real_Estate_Planning).")
    st.stop()

# Add link to switch projects
if st.sidebar.button("Switch Project"):
    st.switch_page("pages/Real_Estate_Planning.py")

st.sidebar.markdown("---")
# Navigation
st.title("Navigation")
page = st.selectbox("Choose a page", ["Main Page", "Quick Start", "Pro-Forma Month", "Amortization Schedule", "Rent Roll"])

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

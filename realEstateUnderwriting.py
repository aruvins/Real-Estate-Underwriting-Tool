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

projects = {
    "Project A": Project(
        name="Project A",
        principal=500000.00,
        start_date=datetime(2024, 1, 1),
        loan_term_years=30,
        annual_interest_rate=3.5,
        monthly_payment=2500.00,
        total_rent=10000.00,
        parking_revenue=500.00,
        laundry_revenue=200.00,
        other_revenue=100.00,
        vacancy_loss=0.05,
        repairs_maintenance=150.00,
        office_expenses=100.00,
        management=300.00,
        payroll=1000.00,
        insurance=400.00,
        r_and_m_account=50.00,
        property_tax=600.00,
        electricity=200.00,
        water_sewer=150.00,
        trash_disposal=50.00,
        misc=75.00
    ),
    "Project B": Project(
        name="Project B",
        principal=750000.00,
        start_date=datetime(2025, 6, 15),
        loan_term_years=25,
        annual_interest_rate=4.0,
        monthly_payment=3500.00,
        total_rent=12000.00,
        parking_revenue=800.00,
        laundry_revenue=300.00,
        other_revenue=150.00,
        vacancy_loss=0.03,
        repairs_maintenance=200.00,
        office_expenses=120.00,
        management=350.00,
        payroll=1200.00,
        insurance=500.00,
        r_and_m_account=80.00,
        property_tax=700.00,
        electricity=250.00,
        water_sewer=180.00,
        trash_disposal=70.00,
        misc=90.00
    )
}

def initialize_session_state():
    default_values = {
        'principal': 0.00,
        'start_date': datetime.today(),
        'loan_term_years': 0,
        'annual_interest_rate': 0.00,
        'monthly_payment': 0.00,
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

# Function to set session state based on selected project
def set_project_values(project):
    project_data = project.to_dict()
    for key, value in project_data.items():
        st.session_state[key] = value
    st.session_state['units'] = project.units

# Initialize session state
initialize_session_state()

# Add project selection page
if "selected_project" not in st.session_state:
    st.title("Project Management")

    # Create a new project
    st.subheader("Create New Project")
    new_project_name = st.text_input("Project Name")
    if st.button("Create New Project"):
        if new_project_name:
            if new_project_name in projects:
                st.error("Project with this name already exists.")
            else:
                # Create and add new project
                new_project = Project(
                    name=new_project_name,
                    principal=0.00,
                    start_date=datetime.today(),
                    loan_term_years=0,
                    annual_interest_rate=0.00,
                    monthly_payment=0.00,
                    total_rent=0.00,
                    parking_revenue=0.00,
                    laundry_revenue=0.00,
                    other_revenue=0.00,
                    vacancy_loss=0.00,
                    repairs_maintenance=0.00,
                    office_expenses=0.00,
                    management=0.00,
                    payroll=0.00,
                    insurance=0.00,
                    r_and_m_account=0.00,
                    property_tax=0.00,
                    electricity=0.00,
                    water_sewer=0.00,
                    trash_disposal=0.00,
                    misc=0.00
                )
                projects[new_project_name] = new_project
                st.success(f"Project '{new_project_name}' created successfully!")
        else:
            st.error("Please enter a project name.")

    # Select an existing project
    st.subheader("Select Project")
    selected_project = st.selectbox("Choose a project", list(projects.keys()), key="project_selector")

    if st.button("Load Project"):
        st.session_state.selected_project = selected_project
        set_project_values(projects[selected_project])
        st.query_params(selected_project=selected_project)

# Continue to main app if project is selected
if "selected_project" in st.session_state:
    st.sidebar.title(f"Current Project: {st.session_state.selected_project}")

    # Custom navigation
    st.title("Navigation")
    page = st.selectbox("Choose a page", ["Main Page", "Quick Start", "Pro-Forma Month", "Amortization Schedule", "Rent Roll"], key="page_selector")

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

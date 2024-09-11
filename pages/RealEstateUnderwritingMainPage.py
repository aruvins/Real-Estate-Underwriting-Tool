import pickle
import streamlit as st
from navi.amortization_schedule import display_amortization_schedule
from navi.rent_roll import display_rent_roll
from navi.main_page import display_main_page
from navi.summary import display_summary
from navi.proforma_month import display_proforma_month
from pages.Real_Estate_Planning import load_projects, projects

PICKLE_FILE = "projects_data.pkl"

# Check if a project is loaded
if "selected_project" not in st.session_state:
    st.warning("No project selected! Please go to the [Project Selection page](./Real_Estate_Planning).")
    st.stop()

def save_projects(projects):
    with open(PICKLE_FILE, 'wb') as f:
        pickle.dump(projects, f)

def auto_save_projects():
    if 'selected_project' in st.session_state:
        project_name = st.session_state['selected_project']
        projects = load_projects()
        if project_name in projects:
            project = projects[project_name]
            # Update all attributes
            for key in project.to_dict().keys():
                if key in st.session_state:
                    setattr(project, key, st.session_state[key])
            # Ensure units data is updated
            if 'units' in st.session_state:
                project.units = st.session_state['units']
            save_projects(projects)

with st.sidebar:
    st.title("📊 Real Estate Tools")
    st.write("`Created by:`")
    linkedin_url = "https://www.linkedin.com/in/aidan-ruvins/"
    st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`Aidan Ruvins`</a>', unsafe_allow_html=True)
        
    st.sidebar.write("---")
    project_name = st.session_state.get('project_name', 'Project Name')
    company_name = st.session_state.get('company_name', 'Your Company')
    st.title(project_name)
    st.subheader(company_name)
    st.write("")
    if st.sidebar.button("Switch Project"):
        st.switch_page("pages/Real_Estate_Planning.py")

    st.sidebar.write("---")

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

# Auto-save any project changes to pickle file
auto_save_projects()

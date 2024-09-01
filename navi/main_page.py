import pandas as pd
import streamlit as st

def display_main_page():
    with st.sidebar:
        project_name = st.session_state.get('project_name', 'Project Name')
        company_name = st.session_state.get('company_name', 'Your Company')
        st.title(project_name)
        st.subheader(company_name)
        st.markdown("---")
        st.title("📊 Real Estate Tools")
        st.write("`Created by:`")
        linkedin_url = "https://www.linkedin.com/in/aidan-ruvins/"
        st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`Aidan Ruvins`</a>', unsafe_allow_html=True)

    st.title("Welcome to Financial Tools")
    st.write("Choose an option from the section above to navigate through different financial tools related to real estate.")

    st.header("Project Name")
    st.session_state.project_name = st.text_input(
        "Project Name", 
        value=st.session_state.get('project_name', 'Project Name')
    )

    st.session_state.company_name = st.text_input(
        "Company Name", 
        value=st.session_state.get('company_name', 'Your Company')
    )

    st.session_state.project_date = st.date_input(
        "Date", 
        value=st.session_state.get('project_date', pd.to_datetime("today").date())
    )

    
import streamlit as st
import pandas as pd

def display_summary():
    with st.sidebar:
        st.title("📊 Summary")
        st.write("`Created by:`")
        linkedin_url = "https://www.linkedin.com/in/aidan-ruvins/"
        st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`Aidan Ruvins`</a>', unsafe_allow_html=True)
    
    st.title("Summary Page")

    st.markdown("---")
    # Sidebar for variable inputs
    st.subheader("Amortization Schedule")

    # Update principal
    st.session_state.principal = st.number_input(
        "Principal Amount", 
        value=st.session_state.principal, 
        step=1000.0
    )

    # Update start date
    st.session_state.start_date = st.date_input(
        "Start Date", 
        value=st.session_state.start_date
    )

    # Update loan term in years
    st.session_state.loan_term_years = st.number_input(
        "Loan Term (Years)", 
        value=st.session_state.loan_term_years, 
        step=1
    )

    # Update annual interest rate
    st.session_state.annual_interest_rate = st.number_input(
        "Annual Interest Rate", 
        value=st.session_state.annual_interest_rate, 
        format="%.2f"
    )

    # Update monthly payment
    st.session_state.monthly_payment = st.number_input(
        "Monthly Payment", 
        value=st.session_state.monthly_payment, 
        format="%.2f"
    )
    st.markdown("---")
    # Manage rent roll
    st.subheader("Manage Rent Roll")
    if st.button("Add New Unit"):
        new_row = pd.DataFrame({'Unit Type': ['New Unit'], 'Rent Price': [0.0], 'Number of Units': [0]})
        st.session_state.units = pd.concat([st.session_state.units, new_row], ignore_index=True, sort=False)

    # Editable DataFrame for rent roll
    edited_df = st.data_editor(
        st.session_state.units, 
        use_container_width=True, 
        key='editable_table_summary', 
        column_config={
            'Unit Type': st.column_config.TextColumn(),
            'Rent Price': st.column_config.NumberColumn(),
            'Number of Units': st.column_config.NumberColumn()
        }
    )

    if st.button('Save Rent Roll Changes'):
        st.session_state.units = edited_df
        st.success("Rent Roll updated successfully!")

    st.markdown("---")
    st.write("Adjust the settings above to see how they affect the results in different pages.")

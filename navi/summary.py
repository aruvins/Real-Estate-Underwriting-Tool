import streamlit as st
import pandas as pd

def display_summary():
    st.title("Summary Page")

    # Input fields for project information
    st.session_state.project.project_name = st.text_input(
        "Project Name", 
        value = st.session_state.project.project_name
    )

    st.session_state.project.company_name = st.text_input(
        "Company Name", 
        value = st.session_state.project.company_name
    )

    st.session_state.project_date = st.date_input(
        "Date", 
        value=st.session_state.get('project_date', pd.to_datetime("today").date())
    )
    
    st.markdown("---")
    st.title("Edit Key Variables")

    # Sidebar for variable inputs
    st.subheader("Amortization Schedule")
    with st.expander("Edit Loans"):
        st.session_state.principal = st.number_input(
            "Principal Amount", 
            value=st.session_state.principal, 
            step=1000.0
        )

        st.session_state.start_date = st.date_input(
            "Start Date", 
            value=st.session_state.start_date
        )

        st.session_state.loan_term_years = st.number_input(
            "Loan Term (Years)", 
            value=st.session_state.loan_term_years, 
            step=1
        )

        st.session_state.annual_interest_rate = st.number_input(
            "Annual Interest Rate", 
            value=st.session_state.annual_interest_rate, 
            format="%.2f"
        )

        st.session_state.monthly_payment = st.number_input(
            "Monthly Payment", 
            value=st.session_state.monthly_payment, 
            format="%.2f"
        )
    
    # Manage rent roll
    st.subheader("Rent Roll")
    with st.expander("Edit Units"):
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

    # Display and edit proforma variables
    st.subheader("Pro-Forma Month")
    with st.expander("Edit Revenue and Expenses"):
        # Revenue and Expense inputs
        st.header("Revenue")
        st.write("Total Monthly Rent")
        st.write(f"{st.session_state.total_rent:.2f}")
        
        st.session_state.parking_revenue = st.number_input(
            "Parking Revenue", 
            value=st.session_state.get('parking_revenue', st.session_state.parking_revenue), 
            format="%.2f"
        )
        st.session_state.laundry_revenue = st.number_input(
            "Laundry Revenue", 
            value=st.session_state.get('laundry_revenue', st.session_state.laundry_revenue), 
            format="%.2f"
        )
        st.session_state.other_revenue = st.number_input(
            "Other Revenue", 
            value=st.session_state.get('other_revenue', st.session_state.other_revenue), 
            format="%.2f"
        )
        st.markdown("---")
        st.header("Expenses")
        st.session_state.vacancy_loss = st.number_input(
            "Vacancy Loss", 
            value=st.session_state.get('vacancy_loss', st.session_state.vacancy_loss), 
            format="%.2f"
        )
        st.session_state.repairs_maintenance = st.number_input(
            "Repairs/Maintenance", 
            value=st.session_state.get('repairs_maintenance', st.session_state.repairs_maintenance), 
            format="%.2f"
        )
        st.session_state.office_expenses = st.number_input(
            "Office Expenses", 
            value=st.session_state.get('office_expenses', st.session_state.office_expenses), 
            format="%.2f"
        )
        st.session_state.management = st.number_input(
            "Management", 
            value=st.session_state.get('management', st.session_state.management), 
            format="%.2f"
        )
        st.session_state.payroll = st.number_input(
            "Payroll", 
            value=st.session_state.get('payroll', st.session_state.payroll), 
            format="%.2f"
        )
        st.session_state.insurance = st.number_input(
            "Insurance", 
            value=st.session_state.get('insurance', st.session_state.insurance), 
            format="%.2f"
        )
        st.session_state.r_and_m_account = st.number_input(
            "R+M Account", 
            value=st.session_state.get('r_and_m_account', st.session_state.r_and_m_account), 
            format="%.2f"
        )
        st.session_state.property_tax = st.number_input(
            "Property Tax", 
            value=st.session_state.get('property_tax', st.session_state.property_tax), 
            format="%.2f"
        )
        st.session_state.electricity = st.number_input(
            "Electricity", 
            value=st.session_state.get('electricity', st.session_state.electricity), 
            format="%.2f"
        )
        st.session_state.water_sewer = st.number_input(
            "Water/Sewer", 
            value=st.session_state.get('water_sewer', st.session_state.water_sewer), 
            format="%.2f"
        )
        st.session_state.trash_disposal = st.number_input(
            "Trash/Disposal", 
            value=st.session_state.get('trash_disposal', st.session_state.trash_disposal), 
            format="%.2f"
        )
        st.session_state.misc = st.number_input(
            "Miscellaneous", 
            value=st.session_state.get('misc', st.session_state.misc), 
            format="%.2f"
        )

    st.markdown("---")
    st.write("Adjust the settings above to see how they affect the results in different pages.")

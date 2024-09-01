# navi/proforma_month.py

import streamlit as st
from Calculators.ProformaMonth import ProformaMonth

def display_proforma_month():
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

    st.title("Proforma Month")
    with st.sidebar:
        # Initialize ProformaMonth object with default values or session state values
        st.title("Revenue")
        st.session_state.total_rent = st.session_state.total_rent
        st.write("Total Monthly Rent")
        st.write(st.session_state.total_rent)
    
        proforma = ProformaMonth(
            parking_revenue=st.number_input("Parking Revenue", value=0.0, step=100.0, format="%.2f"),
            laundry_revenue=st.number_input("Laundry Revenue", value=0.0, step=100.0, format="%.2f"),
            other_revenue=st.number_input("Other Revenue", value=0.0, step=100.0, format="%.2f")
        )

        st.markdown("---")
        st.title("Expenses")
        # Input expenses
        proforma.debt = st.session_state.monthly_payment
        st.write("Monthly Loan Payment")
        st.write(st.session_state.monthly_payment)
        proforma.vacancy_loss = st.number_input("Vacancy Loss", value=0.0, step=100.0, format="%.2f")
        proforma.repairs_maintenance = st.number_input("Repairs/Maintenance", value=0.0, step=100.0, format="%.2f")
        proforma.office_expenses = st.number_input("Office Expenses", value=0.0, step=100.0, format="%.2f")
        proforma.management = st.number_input("Management", value=0.0, step=100.0, format="%.2f")
        proforma.payroll = st.number_input("Payroll", value=0.0, step=100.0, format="%.2f")
        proforma.insurance = st.number_input("Insurance", value=0.0, step=100.0, format="%.2f")
        proforma.r_and_m_account = st.number_input("R+M Account", value=0.0, step=100.0, format="%.2f")
        proforma.property_tax = st.number_input("Property Tax", value=0.0, step=100.0, format="%.2f")
        proforma.electricity = st.number_input("Electricity", value=0.0, step=100.0, format="%.2f")
        proforma.water_sewer = st.number_input("Water/Sewer", value=0.0, step=100.0, format="%.2f")
        proforma.trash_disposal = st.number_input("Trash/Disposal", value=0.0, step=100.0, format="%.2f")
        proforma.misc = st.number_input("Miscellaneous", value=0.0, step=100.0, format="%.2f")

        st.markdown("---")

    # Display Results
    st.subheader(f"Net Operating Income (NOI): ${proforma.calculate_noi():,.2f}")
    st.subheader(f"Debt: ${proforma.debt:,.2f}")
    st.subheader(f"Forward Cash Flow: ${proforma.calculate_forward_cash_flow():,.2f}")

    st.markdown("---")

    # Optionally allow for saving or further processing
    st.session_state.proforma = {
        "Total Revenue": proforma.calculate_total_revenue(),
        "Total Expenses": proforma.calculate_total_expenses(),
        "NOI": proforma.calculate_noi(),
        "Debt": proforma.debt,
        "Forward Cash Flow": proforma.calculate_forward_cash_flow()
    }

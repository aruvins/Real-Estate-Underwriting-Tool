import streamlit as st
import pandas as pd
import altair as alt
from Calculators.ProformaMonth import ProformaMonth

def display_proforma_month():
    with st.sidebar:
        project_name = st.session_state.project.project_name
        st.title(project_name)
        company_name = st.session_state.project.company_name
        st.subheader(company_name)
        st.markdown("---")
        st.title("📊 Real Estate Tools")
        st.write("`Created by:`")
        linkedin_url = "https://www.linkedin.com/in/aidan-ruvins/"
        st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`Aidan Ruvins`</a>', unsafe_allow_html=True)

        st.markdown("---")
        st.title("Revenue")
        st.write("Total Monthly Rent")
        st.write(st.session_state.total_rent, format="%.2f")
        
        proforma = ProformaMonth(
            parking_revenue=st.number_input("Parking Revenue", value=st.session_state.parking_revenue, step=100.0, format="%.2f"),
            laundry_revenue=st.number_input("Laundry Revenue", value=st.session_state.laundry_revenue, step=100.0, format="%.2f"),
            other_revenue=st.number_input("Other Revenue", value=st.session_state.other_revenue, step=100.0, format="%.2f")
        )

        st.markdown("---")
        st.title("Expenses")
        proforma.debt = st.session_state.project.amortization.monthly_payment
        st.write("Monthly Loan Payment")
        st.write(st.session_state.project.amortization.monthly_payment)
        proforma.vacancy_loss = st.number_input("Vacancy Loss", value=st.session_state.vacancy_loss, step=100.0, format="%.2f")
        proforma.repairs_maintenance = st.number_input("Repairs/Maintenance", value=st.session_state.repairs_maintenance, step=100.0, format="%.2f")
        proforma.office_expenses = st.number_input("Office Expenses", value=st.session_state.office_expenses, step=100.0, format="%.2f")
        proforma.management = st.number_input("Management", value=st.session_state.management, step=100.0, format="%.2f")
        proforma.payroll = st.number_input("Payroll", value=st.session_state.payroll, step=100.0, format="%.2f")
        proforma.insurance = st.number_input("Insurance", value=st.session_state.insurance, step=100.0, format="%.2f")
        proforma.r_and_m_account = st.number_input("R+M Account", value=st.session_state.r_and_m_account, step=100.0, format="%.2f")
        proforma.property_tax = st.number_input("Property Tax", value=st.session_state.property_tax, step=100.0, format="%.2f")
        proforma.electricity = st.number_input("Electricity", value=st.session_state.electricity, step=100.0, format="%.2f")
        proforma.water_sewer = st.number_input("Water/Sewer", value=st.session_state.water_sewer, step=100.0, format="%.2f")
        proforma.trash_disposal = st.number_input("Trash/Disposal", value=st.session_state.trash_disposal, step=100.0, format="%.2f")
        proforma.misc = st.number_input("Miscellaneous", value=st.session_state.misc, step=100.0, format="%.2f")

        st.markdown("---")

    st.title("Proforma Month Summary")
            
    # Display Results with Enhanced Styling
    noi = proforma.calculate_noi()
    forward_cash_flow = proforma.calculate_forward_cash_flow()

    # Custom styles for Streamlit
    st.markdown("""
    <style>
        .results-container {
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .results-container h2 {
            color: #ff4b4b;
            margin-bottom: 15px;
        }
        .results-item {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }
        .results-item span.label {
            font-size: 20px;
            font-weight: bold;
            margin-right: 10px;
        }
        .results-item span.value {
            font-size: 24px;
            font-weight: bold;
        }
        .results-item span.noi {
            color: #4CAF50;
        }
        .results-item span.debt {
            color: #FF5722;
        }
        .results-item span.cash-flow {
            color: #2196F3;
        }
    </style>
    """, unsafe_allow_html=True)


    st.markdown(f"""
    <div class="results-item">
        <span class="label">Net Operating Income (NOI):</span>
        <span class="value noi">${noi:,.2f}</span>
    </div>
    <div class="results-item">
        <span class="label">Debt:</span>
        <span class="value debt">${proforma.debt:,.2f}</span>
    </div>
    <div class="results-item">
        <span class="label">Forward Cash Flow:</span>
        <span class="value cash-flow">${forward_cash_flow:,.2f}</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    
    # Store Proforma results in session state
    st.session_state.proforma = {
        "Total Revenue": proforma.calculate_total_revenue(),
        "Total Expenses": proforma.calculate_total_expenses(),
        "NOI": noi,
        "Debt": proforma.debt,
        "Forward Cash Flow": forward_cash_flow
    }
    
    
    # Prepare data for stacked bar chart
    revenue_data = pd.DataFrame({
        'Revenue Type': ['Monthly Rent', 'Parking Revenue', 'Laundry Revenue', 'Other Revenue', 'Total Revenue'],
        'Amount': [
            st.session_state.total_rent,
            proforma.parking_revenue,
            proforma.laundry_revenue,
            proforma.other_revenue,
            st.session_state.total_rent + proforma.parking_revenue + proforma.laundry_revenue + proforma.other_revenue
        ]
    })

    expenses_data = pd.DataFrame({
        'Expense Type': ['Vacancy Loss', 'Repairs/Maintenance', 'Office Expenses', 'Management', 'Payroll', 'Insurance', 'R+M Account', 'Property Tax', 'Electricity', 'Water/Sewer', 'Trash/Disposal', 'Miscellaneous'],
        'Amount': [
            proforma.vacancy_loss,
            proforma.repairs_maintenance,
            proforma.office_expenses,
            proforma.management,
            proforma.payroll,
            proforma.insurance,
            proforma.r_and_m_account,
            proforma.property_tax,
            proforma.electricity,
            proforma.water_sewer,
            proforma.trash_disposal,
            proforma.misc
        ]
    })

    # Stacked Bar Chart: Revenue
    revenue_chart = alt.Chart(revenue_data).mark_bar().encode(
        x=alt.X('Amount:Q', stack='zero'),
        y=alt.Y('Revenue Type:N'),
        text=alt.Text('Amount:Q', format=','),
        color=alt.Color('Revenue Type:N', legend=None)
    ).properties(
        title='Revenue Breakdown'
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_title(
        fontSize=16
    ).configure_text(
        align='left',
        baseline='middle',
        dx=3
    ).configure_legend(
        labelFontSize=12
    )

    # Stacked Bar Chart: Expenses
    expenses_chart = alt.Chart(expenses_data).mark_bar().encode(
        x=alt.X('Amount:Q', stack='zero'),
        y=alt.Y('Expense Type:N'),
        text=alt.Text('Amount:Q', format=','),
        color=alt.Color('Expense Type:N', legend=None)
    ).properties(
        title='Expenses Breakdown'
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_title(
        fontSize=16
    ).configure_text(
        align='left',
        baseline='middle',
        dx=3
    ).configure_legend(
        labelFontSize=12
    )

    # Bar Chart: Total Revenue vs Total Expenses
    breakdown_data = pd.DataFrame({
        'Type': ['Total Revenue', 'Total Expenses'],
        'Amount': [
            proforma.calculate_total_revenue(),
            proforma.calculate_total_expenses()
        ]
    })

    breakdown_chart = alt.Chart(breakdown_data).mark_bar().encode(
        x=alt.X('Type:N', axis=alt.Axis(title='')),
        y=alt.Y('Amount:Q', axis=alt.Axis(title='Amount ($)', format=",.0f")),
        color=alt.Color('Type:N', legend=None),
        text=alt.Text('Amount:Q', format=',')
    ).properties(
        title='Revenue vs Expenses'
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_title(
        fontSize=16
    ).configure_text(
        align='center',
        baseline='middle',
        dy=-5
    )

    st.altair_chart(revenue_chart, use_container_width=True)
    st.altair_chart(expenses_chart, use_container_width=True)
    st.altair_chart(breakdown_chart, use_container_width=True)
    
    st.markdown("---")
    st.write("The Proforma Monthly page provides a detailed financial summary by calculating and displaying key metrics such as Net Operating Income (NOI), Debt, and Forward Cash Flow, alongside visual representations of revenue and expense breakdowns.")

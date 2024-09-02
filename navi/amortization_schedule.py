import streamlit as st
from Calculators.AmortizationSchedule import AmortizationSchedule
from Calculators.Project import Project

def display_amortization_schedule():        
    # Sidebar for User Inputs
    with st.sidebar:
        project_name = st.session_state.project.project_name
        st.title(project_name)
        company_name = st.session_state.project.company_name
        st.subheader(company_name)
        st.markdown("---")
        st.title("📊 Amortization Schedule")
        st.write("`Created by:`")
        linkedin_url = "https://www.linkedin.com/in/aidan-ruvins/"
        st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`Aidan Ruvins`</a>', unsafe_allow_html=True)

        st.session_state.project.amortization.principal = st.number_input("Principal Amount", value = st.session_state.project.amortization.principal, step=1000.0)
        st.session_state.project.amortization.start_date = st.date_input("Start Date", value = st.session_state.project.amortization.start_date)
        st.session_state.project.amortization.loan_term_months = st.number_input("Loan Term (Months)", value = st.session_state.project.amortization.loan_term_months, step=1)
        st.session_state.project.amortization.annual_interest_rate = st.number_input("Annual Interest Rate", value = st.session_state.project.amortization.annual_interest_rate, format="%.2f")
        st.session_state.project.amortization.monthly_payment = st.number_input("Monthly Payment", value = st.session_state.project.amortization.monthly_payment, format="%.2f", step= 100.0)
    
    # Check if graph can be created
    if st.session_state.project.amortization.principal > 0 and st.session_state.project.amortization.loan_term_months > 0:

        # Create Amortization Schedule
        # st.session_state.project.amortization = AmortizationSchedule(
        #     st.session_state.project.amortization.principal,
        #     st.session_state.project.amortization.start_date,
        #     st.session_state.project.amortization.loan_term_months,
        #     st.session_state.project.amortization.annual_interest_rate / 100,
        #     st.session_state.project.amortization.monthly_payment
        # )
        schedule = st.session_state.project.amortization.generate_schedule()

        # Main Page for Output Display
        st.title("Amortization Schedule")

        # Collapsible Amortization Schedule Table
        with st.expander("View Amortization Schedule"):
            st.subheader("Amortization Schedule Table")
            st.table(schedule)

        # Plotting Total Interest and Principal Payments Over Time
        st.subheader("Total Principal and Interest Paid Over Time")

        schedule['Cumulative Principal'] = schedule['Principal'].cumsum()
        schedule['Cumulative Interest'] = schedule['Interest'].cumsum()

        chart_data = schedule[['Month', 'Cumulative Principal', 'Cumulative Interest']].melt(id_vars='Month', var_name='Payment Type', value_name='Amount')
        st.line_chart(chart_data.pivot(index='Month', columns='Payment Type', values='Amount'))

        st.markdown("---")
        st.write("This schedule illustrates how much of each payment goes toward interest and how much goes toward paying off the principal. Over time, the interest portion decreases as the principal is paid down.")
    
    else:
        st.warning("Please enter a principal amount greater than $0.00 to generate the amortization schedule.")
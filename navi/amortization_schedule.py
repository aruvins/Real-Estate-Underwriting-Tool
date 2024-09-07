import streamlit as st
from Calculators.AmortizationSchedule import AmortizationSchedule
from Calculators.Project import Project

def display_amortization_schedule():        
    # Sidebar for User Inputs
    with st.sidebar:
        st.session_state.principal = st.number_input("Principal Amount", value=st.session_state.get('principal', 0.0), step=1000.0)
        st.session_state.start_date = st.date_input("Start Date", value=st.session_state.get('start_date', None))
        st.session_state.loan_term_years = st.number_input("Loan Term (Years)", value=st.session_state.get('loan_term_years', 30), step=1)
        st.session_state.annual_interest_rate = st.number_input("Annual Interest Rate", value=st.session_state.get('annual_interest_rate', 5.0), format="%.2f")
        st.session_state.monthly_payment = st.number_input("Monthly Payment", value=st.session_state.get('monthly_payment', 0.0), format="%.2f")

    # Check if principal is greater than zero
    if st.session_state.principal > 0:
        # Convert years to months
        loan_term_months = int(st.session_state.loan_term_years * 12)

        # Create Amortization Schedule
        amortization = AmortizationSchedule(
            st.session_state.principal,
            st.session_state.start_date.strftime("%Y-%m-%d"),
            loan_term_months,
            st.session_state.annual_interest_rate / 100,
            st.session_state.monthly_payment
        )
        schedule = amortization.generate_schedule()

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
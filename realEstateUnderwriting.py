import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Real Estate Underwriting",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Amortization Schedule Class
class AmortizationSchedule:
    def __init__(self, principal, start_date, loan_term_months, annual_interest_rate, monthly_payment):
        self.principal = principal
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.loan_term_months = loan_term_months
        self.annual_interest_rate = annual_interest_rate
        self.monthly_interest_rate = annual_interest_rate / 12
        self.monthly_payment = monthly_payment
    
    def calculate_monthly_interest(self, remaining_balance):
        return remaining_balance * self.monthly_interest_rate
    
    def calculate_principal_payment(self, monthly_interest):
        return self.monthly_payment - monthly_interest
    
    def generate_schedule(self):
        schedule = []
        remaining_balance = self.principal
        current_date = self.start_date
        
        for month in range(1, self.loan_term_months + 1):
            monthly_interest = self.calculate_monthly_interest(remaining_balance)
            principal_payment = self.calculate_principal_payment(monthly_interest)
            remaining_balance -= principal_payment
            
            if remaining_balance < 0:
                principal_payment += remaining_balance
                remaining_balance = 0
            
            schedule.append({
                "Month": month,
                "Date": current_date.strftime("%Y-%m-%d"),
                "Payment": round(self.monthly_payment, 2),
                "Principal": round(principal_payment, 2),
                "Interest": round(monthly_interest, 2),
                "Remaining Balance": round(remaining_balance, 2)
            })
            
            current_date += timedelta(days=30)  # Approximate to next month
        
        return pd.DataFrame(schedule)

st.title("Navigation")
page = st.selectbox("Choose a page", ["Main Page", "Amortization Schedule"])

if page == "Main Page":
    with st.sidebar:
        st.title("📊 Real Estate Tools")
        st.write("`Created by:`")
        linkedin_url = "https://www.linkedin.com/in/aidan-ruvins/"
        st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`Aidan Ruvins`</a>', unsafe_allow_html=True)

    st.title("Welcome to Financial Tools")
    st.write("Choose an option from the section above to navigate through different financial tools related to real estate.")



elif page == "Amortization Schedule":
    # Sidebar for User Inputs
    with st.sidebar:
        st.title("📊 Amortization Schedule")
        st.write("`Created by:`")
        linkedin_url = "https://www.linkedin.com/in/aidan-ruvins/"
        st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`Aidan Ruvins`</a>', unsafe_allow_html=True)

        principal = st.number_input("Principal Amount", value=500000.0)
        start_date = st.date_input("Start Date", value=datetime(2024, 9, 1))
        loan_term_years = st.number_input("Loan Term (Years)", value=30)
        annual_interest_rate = st.number_input("Annual Interest Rate", value=0.04)
        monthly_payment = st.number_input("Monthly Payment", value=2387.08)

    # Convert years to months
    loan_term_months = int(loan_term_years * 12)

    # Create Amortization Schedule
    amortization = AmortizationSchedule(principal, start_date.strftime("%Y-%m-%d"), loan_term_months, annual_interest_rate, monthly_payment)
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
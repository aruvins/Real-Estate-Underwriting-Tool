import streamlit as st
import pandas as pd
from datetime import datetime
from Calculators.AmortizationSchedule import AmortizationSchedule
from Calculators.RentRoll import RentRoll

# Page configuration
st.set_page_config(
    page_title="Real Estate Underwriting",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables if not already present
if 'principal' not in st.session_state:
    st.session_state.principal = 500000.0
if 'start_date' not in st.session_state:
    st.session_state.start_date = datetime(2024, 9, 1)
if 'loan_term_years' not in st.session_state:
    st.session_state.loan_term_years = 30
if 'annual_interest_rate' not in st.session_state:
    st.session_state.annual_interest_rate = 0.04
if 'monthly_payment' not in st.session_state:
    st.session_state.monthly_payment = 2387.08

# Initialize session state for rent roll if not already present
if 'units' not in st.session_state or st.session_state.units.empty:
    # Start with a default row
    st.session_state.units = pd.DataFrame([{'Unit Type': 'New Unit', 'Rent Price': 0.0, 'Number of Units': 0}])

st.title("Navigation")
page = st.selectbox("Choose a page", ["Main Page", "Amortization Schedule", "Rent Roll"])

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

        st.session_state.principal = st.number_input("Principal Amount", value=st.session_state.principal, step=1000.0)
        st.session_state.start_date = st.date_input("Start Date", value=st.session_state.start_date)
        st.session_state.loan_term_years = st.number_input("Loan Term (Years)", value=st.session_state.loan_term_years, step=1)
        st.session_state.annual_interest_rate = st.number_input("Annual Interest Rate", value=st.session_state.annual_interest_rate, format="%.2f")
        st.session_state.monthly_payment = st.number_input("Monthly Payment", value=st.session_state.monthly_payment, format="%.2f")

    # Convert years to months
    loan_term_months = int(st.session_state.loan_term_years * 12)

    # Create Amortization Schedule
    amortization = AmortizationSchedule(
        st.session_state.principal,
        st.session_state.start_date.strftime("%Y-%m-%d"),
        loan_term_months,
        st.session_state.annual_interest_rate,
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

elif page == "Rent Roll":
    with st.sidebar:
        st.title("📊 Rent Roll")
        st.write("`Created by:`")
        linkedin_url = "https://www.linkedin.com/in/aidan-ruvins/"
        st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`Aidan Ruvins`</a>', unsafe_allow_html=True)

    st.title("Rent Roll")

    # Manage Rent Roll
    st.subheader("Manage Rent Roll")

    # Button to add a new row with default values
    if st.button("Add New Unit"):
        # Create a new row with default values
        new_row = pd.DataFrame({'Unit Type': ['New Unit'], 'Rent Price': [0.0], 'Number of Units': [0]})
        # Append the new row to the existing DataFrame
        st.session_state.units = pd.concat([st.session_state.units, new_row], ignore_index=True, sort=False)

    # Editable DataFrame
    edited_df = st.data_editor(st.session_state.units, use_container_width=True, key='editable_table', column_config={
        'Unit Type': st.column_config.TextColumn(),
        'Rent Price': st.column_config.NumberColumn(),
        'Number of Units': st.column_config.NumberColumn()
    })

    # Submit button to update session state
    if st.button('Save Changes'):
        st.session_state.units = edited_df
        st.success("Rent Roll updated successfully!")

    # Create Rent Roll
    rent_roll = RentRoll()
    for _, row in st.session_state.units.iterrows():
        rent_roll.add_unit_type(row['Unit Type'], row['Rent Price'])
        rent_roll.set_unit_count(row['Unit Type'], row['Number of Units'])

    rent_roll_df = rent_roll.generate_rent_roll()
    total_rent = rent_roll.calculate_total_rent()

    # Display Rent Roll
    if rent_roll_df.empty:
        st.write("**No unit types have been added yet. Please add unit types and their corresponding rent prices in the table.**")
    else:
        st.markdown("---")
        # Display Total Rent
        st.subheader("Total Monthly Rent")
        st.write(f"Total Monthly Rent: ${total_rent:,.2f}")

        # Rent Roll Table
        with st.expander("View Rent Roll Table"):
            st.subheader("Rent Roll Table")
            st.table(rent_roll_df)

        # Plotting Rent by Unit Type
        st.subheader("Rent Breakdown by Unit Type")
        
        # Ensure the DataFrame has the expected columns
        if 'Unit Type' in rent_roll_df.columns and 'Total Rent' in rent_roll_df.columns:
            rent_chart_data = rent_roll_df[['Unit Type', 'Total Rent']]
            st.bar_chart(rent_chart_data.set_index('Unit Type'))
        else:
            st.error("The expected columns 'Unit Type' and 'Total Rent' are not found in the DataFrame.")

    st.markdown("---")
    st.write("The rent roll provides a breakdown of the total rent by unit type, including a visual representation and the total monthly rent.")

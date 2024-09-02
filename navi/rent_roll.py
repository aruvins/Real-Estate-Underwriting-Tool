import streamlit as st
import pandas as pd
from Calculators.RentRoll import RentRoll

def display_rent_roll():
    with st.sidebar:
        project_name = st.session_state.project.project_name
        st.title(project_name)
        company_name = st.session_state.project.company_name
        st.subheader(company_name)
        st.markdown("---")
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
        new_row = pd.DataFrame({'Unit Type': ['New Unit'], 'Rent Price': [0.00], 'Number of Units': [0]})
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
    st.session_state.total_rent = rent_roll.calculate_total_rent()

    # Display Rent Roll
    if rent_roll_df.empty:
        st.write("**No unit types have been added yet. Please add unit types and their corresponding rent prices in the table.**")
    else:
        st.markdown("---")
        # Display Total Rent
        st.subheader("Total Monthly Rent")
        st.write(f"Total Monthly Rent: ${st.session_state.total_rent:,.2f}")

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
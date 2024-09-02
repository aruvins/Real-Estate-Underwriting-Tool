import streamlit as st
from Calculators.RentRoll import RentRoll
from Calculators.AmortizationSchedule import AmortizationSchedule

class ProformaMonth:
    def __init__(self, parking_revenue, laundry_revenue, other_revenue):
        # Revenue Variables
        self.debt = st.session_state.project.amortization.monthly_payment
        self.rent_roll_total = st.session_state.total_rent
        self.parking_revenue = parking_revenue
        self.laundry_revenue = laundry_revenue
        self.other_revenue = other_revenue
        
        # Expense Variables
        self.vacancy_loss = 0.0
        self.repairs_maintenance = 0.0
        self.office_expenses = 0.0
        self.management = 0.0
        self.payroll = 0.0
        self.insurance = 0.0
        self.r_and_m_account = 0.0
        self.property_tax = 0.0
        self.electricity = 0.0
        self.water_sewer = 0.0
        self.trash_disposal = 0.0
        self.misc = 0.0

    def calculate_total_revenue(self):
        return self.rent_roll_total + self.parking_revenue + self.laundry_revenue + self.other_revenue

    def calculate_total_expenses(self):
        totalExpenses = self.vacancy_loss + self.repairs_maintenance + self.office_expenses + self.management + self.payroll + self.insurance + self.r_and_m_account + self.property_tax + self.electricity + self.water_sewer + self.trash_disposal + self.misc
        return totalExpenses

    def calculate_noi(self):
        return self.calculate_total_revenue() - self.calculate_total_expenses()

    def calculate_forward_cash_flow(self):
        return self.calculate_noi() - self.debt

import pandas as pd


class Project:
    def __init__(self, name, principal, start_date, loan_term_years, annual_interest_rate, monthly_payment,
                 total_rent, parking_revenue, laundry_revenue, other_revenue, vacancy_loss, repairs_maintenance,
                 office_expenses, management, payroll, insurance, r_and_m_account, property_tax, electricity,
                 water_sewer, trash_disposal, misc):
        self.name = name
        self.principal = principal
        self.start_date = start_date
        self.loan_term_years = loan_term_years
        self.annual_interest_rate = annual_interest_rate
        self.monthly_payment = monthly_payment
        self.total_rent = total_rent
        self.parking_revenue = parking_revenue
        self.laundry_revenue = laundry_revenue
        self.other_revenue = other_revenue
        self.vacancy_loss = vacancy_loss
        self.repairs_maintenance = repairs_maintenance
        self.office_expenses = office_expenses
        self.management = management
        self.payroll = payroll
        self.insurance = insurance
        self.r_and_m_account = r_and_m_account
        self.property_tax = property_tax
        self.electricity = electricity
        self.water_sewer = water_sewer
        self.trash_disposal = trash_disposal
        self.misc = misc
        self.units = pd.DataFrame([{'Unit Type': 'New Unit', 'Rent Price': 0.00, 'Number of Units': 0}])

    def to_dict(self):
        return {
            'principal': self.principal,
            'start_date': self.start_date,
            'loan_term_years': self.loan_term_years,
            'annual_interest_rate': self.annual_interest_rate,
            'monthly_payment': self.monthly_payment,
            'total_rent': self.total_rent,
            'parking_revenue': self.parking_revenue,
            'laundry_revenue': self.laundry_revenue,
            'other_revenue': self.other_revenue,
            'vacancy_loss': self.vacancy_loss,
            'repairs_maintenance': self.repairs_maintenance,
            'office_expenses': self.office_expenses,
            'management': self.management,
            'payroll': self.payroll,
            'insurance': self.insurance,
            'r_and_m_account': self.r_and_m_account,
            'property_tax': self.property_tax,
            'electricity': self.electricity,
            'water_sewer': self.water_sewer,
            'trash_disposal': self.trash_disposal,
            'misc': self.misc
        }
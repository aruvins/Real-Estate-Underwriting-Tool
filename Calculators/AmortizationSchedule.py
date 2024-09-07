import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

class AmortizationSchedule:
    def __init__(self, principal, start_date, loan_term_months, annual_interest_rate, monthly_payment):
        self.principal = principal
        self.start_date = start_date
        self.loan_term_months = loan_term_months
        self.annual_interest_rate = annual_interest_rate
        self.monthly_interest_rate = annual_interest_rate / 12
        self.monthly_payment = monthly_payment
    
    def getMonthlyPayment(self):
        return self.monthly_payment
    
    def calculate_monthly_interest(self, remaining_balance):
        return (remaining_balance * self.monthly_interest_rate)
    
    def calculate_principal_payment(self, monthly_interest):
        return self.monthly_payment - monthly_interest
    
    def generate_schedule(self):
        schedule = []
        remaining_balance = self.principal
        current_date = self.start_date
        
        for month in range(1, self.loan_term_months + 1):
            monthly_interest = self.calculate_monthly_interest(remaining_balance)
            principal_payment = self.calculate_principal_payment(monthly_interest)
            
            if remaining_balance < principal_payment:
                principal_payment = remaining_balance
                self.monthly_payment = monthly_interest + principal_payment
                remaining_balance = 0
            else:
                remaining_balance -= principal_payment
            
            schedule.append({
                "Month": month,
                "Date": current_date.strftime("%Y-%m-%d"),
                "Payment": round(self.monthly_payment, 2),
                "Principal": round(principal_payment, 2),
                "Interest": round(monthly_interest, 2),
                "Remaining Balance": round(remaining_balance, 2)
            })
            
            current_date += relativedelta(months=1)  # Use relativedelta for accurate month-end calculation
        
        return pd.DataFrame(schedule)
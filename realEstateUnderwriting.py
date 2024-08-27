import pandas as pd
from datetime import datetime, timedelta

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

# Example usage:
principal = 5104822  # Principal amount
start_date = "2024-01-01"  # Loan start date
loan_term_months = 360  # Loan term in months (30 years)
annual_interest_rate = 0.0371  # 4% annual interest rate
monthly_payment = 23526.00  # Monthly payment amount

amortization = AmortizationSchedule(principal, start_date, loan_term_months, annual_interest_rate, monthly_payment)
schedule = amortization.generate_schedule()
print(schedule)
import streamlit as st
import pandas as pd
from datetime import datetime

from Calculators.AmortizationSchedule import AmortizationSchedule
# from Calculators.RentRoll import RentRoll
# from Calculators.ProformaMonth import ProformaMonth

class Project:
    def __init__(self):
        self.project_name = "Project Name"
        self.company_name = "Your Company"
        self.amortization = AmortizationSchedule(0.00, datetime.today(), 0, 0.00, 0.00)
        # self.rentRoll = RentRoll()
        # self.proformaMonth = ProformaMonth()

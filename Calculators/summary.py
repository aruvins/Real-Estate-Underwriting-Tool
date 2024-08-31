import pandas as pd

class Summary:
    def __init__(self, project_name, analyst, date, equity_gp, equity_lp, tranche1, purchase_price, tax_escrow, finance_cost, 
                 dscr_min, cash_on_cash_min, multiple, irr_levered, irr_unlevered, rent_per_unit, num_units, rent_per_month,
                 management_fee, repairs_maintenance, office_expense, misc_expense, electricity, water_sewer, property_tax, 
                 insurance, trash_disposal, payroll, cap_rate, sales_expense, discount_rate, sale_period, refi_period):
        self.project_name = project_name
        self.analyst = analyst
        self.date = date
        self.equity_gp = equity_gp
        self.equity_lp = equity_lp
        self.tranche1 = tranche1
        self.purchase_price = purchase_price
        self.tax_escrow = tax_escrow
        self.finance_cost = finance_cost
        self.dscr_min = dscr_min
        self.cash_on_cash_min = cash_on_cash_min
        self.multiple = multiple
        self.irr_levered = irr_levered
        self.irr_unlevered = irr_unlevered
        self.rent_per_unit = rent_per_unit
        self.num_units = num_units
        self.rent_per_month = rent_per_month
        self.management_fee = management_fee
        self.repairs_maintenance = repairs_maintenance
        self.office_expense = office_expense
        self.misc_expense = misc_expense
        self.electricity = electricity
        self.water_sewer = water_sewer
        self.property_tax = property_tax
        self.insurance = insurance
        self.trash_disposal = trash_disposal
        self.payroll = payroll
        self.cap_rate = cap_rate
        self.sales_expense = sales_expense
        self.discount_rate = discount_rate
        self.sale_period = sale_period
        self.refi_period = refi_period
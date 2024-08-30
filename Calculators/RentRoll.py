import pandas as pd

class RentRoll:
    def __init__(self):
        self.unit_prices = {}  # Dictionary to store rent prices for each unit type
        self.unit_counts = {}  # Dictionary to store counts of each unit type

    def add_unit_type(self, unit_type, rent_price):
        """
        Add a new unit type with its rent price.

        Parameters:
        unit_type (str): Description of the unit type (e.g., '1 bed 1 bath')
        rent_price (float): Rent price for the unit type
        """
        self.unit_prices[unit_type] = rent_price

    def set_unit_count(self, unit_type, count):
        """
        Set the number of units for a specific unit type.

        Parameters:
        unit_type (str): Description of the unit type
        count (int): Number of units of this type
        """
        if unit_type in self.unit_prices:
            self.unit_counts[unit_type] = count
        else:
            raise ValueError(f"Unit type '{unit_type}' not found. Please add it first.")

    def calculate_total_rent(self):
        """
        Calculate the total monthly rent based on the unit counts and rent prices.

        Returns:
        float: Total monthly rent
        """
        total_rent = 0.0
        for unit_type, count in self.unit_counts.items():
            rent_price = self.unit_prices.get(unit_type, 0)
            total_rent += rent_price * count
        return total_rent

    def generate_rent_roll(self):
        """
        Generate a DataFrame representing the rent roll.

        Returns:
        pd.DataFrame: DataFrame with unit type, count, and total rent for each unit type
        """
        data = []
        for unit_type, count in self.unit_counts.items():
            rent_price = self.unit_prices.get(unit_type, 0)
            total_rent = rent_price * count
            data.append({
                "Unit Type": unit_type,
                "Count": count,
                "Rent Price per Unit": rent_price,
                "Total Rent": total_rent
            })
        return pd.DataFrame(data)

# Example usage
rent_roll = RentRoll()
rent_roll.add_unit_type("1 bed 1 bath", 1200)
rent_roll.add_unit_type("2 bed 2 bath", 1800)
rent_roll.set_unit_count("1 bed 1 bath", 10)
rent_roll.set_unit_count("2 bed 2 bath", 5)

# Calculate total rent
total_rent = rent_roll.calculate_total_rent()
print(f"Total Monthly Rent: ${total_rent:,.2f}")

# Generate rent roll DataFrame
rent_roll_df = rent_roll.generate_rent_roll()
print(rent_roll_df)

"""
File: investment.py
Author: Your Name
Date: Creation or modification date in YYYY-MM-DD format
Description: A brief explanation of what this program does.
"""

# Ask for user input
principal_amount = float(input("Enter Principal Amount: "))
interest_rate = float(input("Enter Annual Interest Rate: "))
num_years = int(input("Enter Number of  Years: "))

# Calculate future value by multiply
future_value = principal_amount * (1+interest_rate)**num_years

# Output result
print("Result: Future Value of investment is " + str(future_value))
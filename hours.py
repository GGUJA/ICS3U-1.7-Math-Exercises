"""
File: hours.py
Author: Your Name
Date: Creation or modification date in YYYY-MM-DD format
Description: A brief explanation of what this program does.
"""

# Ask for user input
hour = int(input("Enter Duration in hours: "))

# Calculate days and hour_left
days = int(hour / 24)
hour_left = int(hour - (days * 24))

# Output result
print("Result: " + str(hour) + " hours is equal to " + str(days) + " days, " + str(hour_left) + " hours")
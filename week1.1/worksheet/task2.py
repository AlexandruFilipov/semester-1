"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""
import math
name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")
amount = 0
# Ask the user to input an amount they want to save every month - this should be an integer.

amount = int(input("enter the amount of money you want to save every month"))
# Validate that they have entered an integer.


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
total = amount*12
# print this out for the user with a suitable message.
print("The total amount of money you will save will be", total) 


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
total2 = total * 1.08
# print this out in the format £X.XX (to two decimal places).
print("The total after interest will be £",round(total2,2))

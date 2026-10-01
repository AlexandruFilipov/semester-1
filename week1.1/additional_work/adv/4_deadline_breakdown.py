"""Advanced Task 4: Deadline Breakdown
- Ask how many minutes remain until an assignment deadline.
- Use integer division and modulo to convert this number into days, hours, and minutes.
- Present the result using a formatted string such as "2 days, 3 hours, 15 minutes remaining".
- Extension: handle negative input by printing a warning that the deadline has already passed.
"""
import math
minutes_remaining_input = input("Minutes remaining until the deadline: ")

# TODO: convert the input to an integer
minutes_remaining_input = int(minutes_remaining_input)
# TODO: calculate whole days, leftover hours, and remaining minutes
hours = (minutes_remaining_input / 60)
days = (hours / 24)
hours = (hours%24)
minutes_remaining_input = (minutes_remaining_input%60)
days = round(days,0)
hours = round(hours,0)
if hours < 1:
    hours = 0
if days < 1:
    days = 0

# TODO: print the breakdown using f-strings
print(f"{days}, days,{hours}, hours,{minutes_remaining_input}, minutes")
# Extension: detect negative values and print a warning instead

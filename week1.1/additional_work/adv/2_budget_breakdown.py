"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""
import math
travel_cost_input = input("Travel cost in pounds: ")
food_cost_input = input("Food cost in pounds: ")
accommodation_cost_input = input("Accommodation cost in pounds: ")

# TODO: convert each value to a number type that supports decimals
travel_cost_input = int(travel_cost_input)
food_cost_input = int(food_cost_input)
accommodation_cost_input = int(accommodation_cost_input)
# TODO: calculate the total and the average spend per category
total = travel_cost_input + accommodation_cost_input + food_cost_input
# TODO: print the three costs, the total, and the average
# Extension: format the totals to two decimal places

average = total/3
travel_cost_input = round((travel_cost_input),2)
food_cost_input = round((food_cost_input),2)
accommodation_cost_input = round((accommodation_cost_input),2)
total = round((total),2)
average = round((average),2)
print(travel_cost_input)
print(food_cost_input)
print(accommodation_cost_input)
print(average)

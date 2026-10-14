# Worksheet 1.2: Task 1 Solution
import sys

try:
  grade = int(input("Enter your number between 0-100: "))
  if grade > 100 or grade < 0:
    sys.exit("Error: Grade must be an integer between 0 and 100")
except ValueError:
  sys.exit("Error: Grade must be an integer between 0 and 100")


result = "N/A"
if grade >= 0 and grade < 40:
  result = "Fail"
elif grade < 70 and grade >= 40:
  result = "Pass"
else: 
  result = "Distinction"

print(f"{grade} is a {result}")

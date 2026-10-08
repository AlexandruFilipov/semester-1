# Worksheet 1.2: Task 1 Solution
try:
  grade = int(input("Enter your number between 0-100: "))
  if grade > 100 and grade < 0:
    print("Error: Grade must be an integer between 0 and 100")
    exit()
except ValueError:
  print("Error: Grade must be an integer between 0 and 100")
  exit()


result = "N/A"
if grade > 0 and grade < 40:
  result = "Fail"
elif grade < 70 and grade >= 40:
  result = "Pass"
else: 
  result = "Distinction"

print(result)

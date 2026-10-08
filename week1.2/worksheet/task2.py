# Worksheet 1.2: Task 2 Solution
from util import read_numbers
numbers = read_numbers()
if numbers == []:
  print("Error: no numbers provided")
  sys.exit()

minimum = min(numbers)
maximum = max(numbers)
mean = mean(numbers)
median = median(numbers)
print(f"Minimum = "{minimum})
print(f"Maximum = "{maximum})
print(f"mean = "{mean})
print(f"median = "{median})
jjhjh
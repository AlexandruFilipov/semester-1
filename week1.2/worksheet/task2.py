# Worksheet 1.2: Task 2 Solution
from util import read_numbers
numbers = read_numbers()
if numbers == [] :
  print("Error: no numbers provided")
  exit()

print(numbers)
minimum = min(numbers)
maximum = max(numbers)
median = 0
mean = 0
mean = sum(numbers) 
mean = (mean / len(numbers))
numbers2 = []
index = 0
filler = 0

numbers.sort()
if len(numbers) % 2 != 0:
  index = (len(numbers)//2)
  median = numbers[index]
elif len(numbers) % 2 == 0:
  index = (len(numbers)//2)
  filler = numbers[index]
  index -= 1
  filler += numbers[index]
  median = filler / 2

print(f"Minimum = ",(minimum))
print(f"Maximum = ",(maximum))
print(f"Mean = ",(mean))
print(f"Median = ",(median))

# Write a program to make use of map(), filter() and reduce() functions with context to lambda functions.
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_numbers)

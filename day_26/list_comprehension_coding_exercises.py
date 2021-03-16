'''
# Interactive Coding Exercise 1:
# Using list comprehension to take numbers from a list and squaring them and
# putting them into another list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
# Alternatively, we can use exponents:
# squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

# Interactive Coding Exercise 2:
# Using list comprehension to take even numbers from list and putting them
# into another list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print(result)
'''
# Interactive Coding Exercise 3:
# Using list comprehension, create a list containing numbers that are common
# within two files
with open("file_1.txt") as file_1:
    file_one_numbers = file_1.readlines()

with open("file_2.txt") as file_2:
    file_two_numbers = file_2.readlines()

print(file_one_numbers)
print(file_two_numbers)

results = [int(num) for num in file_one_numbers if num in file_two_numbers]
print(results)






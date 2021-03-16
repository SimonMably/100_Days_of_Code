print()
# List comprehension is where we can create a new list from a previous list.
'''
numbers = [1, 2, 3]
new_list = []
for n in list:
    add_1 = n + 1
new_list.append(add_1)
'''
# We can do this using a 'keyword' method. eg,
'''new_list = ['new_item' for 'item' in 'list']'''
# With this method, we just need to replace all of the keywords (the words
# within single-quote marks) with whatever we need

# With list comprehension and the 'keyword' method, the above code becomes:
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
# 'new_item' becomes 'n + 1', 'item' becomes 'n', and 'list' becomes 'numbers'

# List comprehension can also be used strings as well.
name = "Simon"
new_name_list = [letter for letter in name]
# Puts each letter in name variable in a list
print(new_name_list)

# Python sequences: list, range, string, tuple
# These are sequences because they have a specific order and when we perform
# a list comprehension on them, the list comprehension takes that sequence
# and it will go though it in order (whether its letters in a string or
# integers in a list) and it will do something with each item in that sequence.

# Challenge: use range() to get numbers from 1 to 4, and then double them
# with list comprehension

range_list = [number * 2 for number in range(1, 5)]
print(range_list)


# Conditional List Comprehension
# A conditional list comprehensions is like a regular list comprehension,
# except it has an if statement at the end of it. 'keyword' method example:
'''new_list = ["new_item" for "item" in "list" if "test"]'''
# This means that it will do the "action" on "each item" in "the thing" if it
# passes the "condition".

# Using a conditional list comprehension to use short names in a list
names = ["Alex", "Beth", "Dave", "Caroline", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
# 'short_names' will only contain "Alex", "Beth" and "Dave"
print(short_names)

# Challenge: Using list comprehension, from 'names' get names longer than 5
# characters and put them in a new list and make all letters in each name
# upper case.
uppercase_names = [name.upper() for name in names if len(name) > 5]
print(uppercase_names)

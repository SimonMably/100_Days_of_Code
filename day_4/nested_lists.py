# When working with list, a common problem is the ocuurance of the IndexError
# (displays: 'IndexError: list index out of range')

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", 
                    "Connecticut", "Massachusetts", "Maryland", 
                    "South Carolina", "New Hampshire", "Virginia", "New York", 
                    "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
                    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", 
                    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", 
                    "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
                    "California", "Minnesota", "Oregon", "Kansas", 
                    "West Virginia", "Nevada", "Nebraska", "Colorado", 
                    "North Dakota", "South Dakota", "Montana", "Washington", 
                    "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", 
                    "Arizona", "Alaska", "Hawaii"]



# Printing an entire list
print(states_of_america[49])  # Prints last item in list
'''
print(states_of_america[50])  # Returns IndexError: list index out of range
                              # because there is not list item at index postion
                              # 50'''

# Using the len() function to find out how many items are in a list
print(len(states_of_america))

# Using the len() function in another way
num_of_states = len(states_of_america)

# print(states_of_america[num_of_states])
# Using this will return the IndexError because the len() will return '50' and 
# lists indexs have an 'off-by-one' functionality, where a lists index starts
# at '0'. This is why the IndexError will happen.

# To get around the above problem, the code on line 32 can be modified slightly:
print(states_of_america[num_of_states - 1])

# Nested lists
'''
# Original list
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", 
                "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", 
                "Potatoes"]
'''

# 1 way to get a nested list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", 
            "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# The Nested List:
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
# Printing 'dirty_dozen' prints 2 lists inside a list.

# Accessing specific lists and items from nested lists:

# This will print the fruits list from inside dirty_dozen
print(dirty_dozen[0])  

# This will print the vegetable list from inside dirty_dozen
print(dirty_dozen[1])  

# This will print Grapes from fruits list from dirty_dozen
print(dirty_dozen[0][3])  

# This will print Kale from fruits list from dirty_dozen
print(dirty_dozen[1][1])  








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
print(states_of_america)

# Printing a specific item in the list. The number within the square brackets
# indicte the index position of the item within the list (index positions start
# at 0)
print(states_of_america[0])

# If we need to print the last item of the list, we can use -1 as the index 
# (and use proceeding negative numbers if we want to print the list in a back
# to front kind of fashion).
print(states_of_america[-1])

# Changing an item within a list
# Before change:
print(f"Before Change: {states_of_america[1]}")
# After change:
states_of_america[1] = "Pencilvania"
print(f"After Change: {states_of_america[1]}")

# Appending an item to the end of a list with the append() function.
states_of_america.append("Simonland")

# Using the extend() function to insert a bunch of items onto the end of a list
states_of_america.extend(["Simontopia", "North Simon", "South Simon"])

print(states_of_america)

# See what else can be done with lists here:
# https://docs.python.org/3/tutorial/datastructures.html
print("\nSee what else can be done with lists here:\n"
    "https://docs.python.org/3/tutorial/datastructures.html")


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", 
                "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", 
                "Potatoes"]








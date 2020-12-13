fruits = ["Apple", "Peach", "Pear"]

# Using a for loop to print each item in the fruits list
for fruit in fruits:
    print(fruit)
# What a for loop means is: 
    # for each item in this thing:
        # do this thing / do these things

# In the above for loop, it means:
# for *each fruit* in *the fruits list*:
    # print *each fruit*

# How for loops work:
    # In the fruits list above, the for loop takes the fruits list and asigns 
    # the variable name 'fruit' to each item in the fruits list. Then, the for
    # loop will perform whatever actions are on its indented line. In this case,
    # the for loop will print each item in the fruits list upon each 
    # iteration/loop of this particular for loop.
    # On the first loop, the 'fruit' variable name will be asigned to 'Apple',
    # then 'Peach' on the second loop, and then 'Pear' on the last loop.

print()

# Adding to the above for loop:
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie\n")
    print(fruits)
print(fruits)
# We can add as many actions to a for loop, as long as the actions indented
# directly underneath the for loop line.
# It's important to make sure that if an action is intended to be within a for
# loop, that action should be directly underneath the for loop line *AND* indented. 
# Any action underneath the for loop line *AND NOT* indented will not be apart
# of the for loop and will not be executed until after the for loop has finished.



















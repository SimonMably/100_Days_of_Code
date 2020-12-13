# While loop syntax:
'''
while condition_is_True:
    do this
    and do this
    and do this 
    and do this
    finally, this this
'''

# Difference between a for loop and a while loop:

# for loop:
'''
Iterates over a string, a collection of items, or a range of things using the 
range() function and performs an action(s) upon each item within whatever the 
for loop is iterating over. The for loop will end on the last item.
'''

# while loop:
'''
The while loop will perform a loop while a condition is True (or False). 

Example:

variable = 0
while variable <= 10:
    variable += 1
    print(variable)

While the condition in the example while loop is True, the code within the while
loops code block will execute by adding 1 to/printing variable. This while loop
will keep doing this until variable is equal to 10 (when the condition is 
False), at which point the while loop will stop.
'''

# Which to use:
'''
Use a for loop to iterate over a collection or range and something needs to 
happen for each item in the collection/range.
Use a for loop on collections that are known to have an end.

Use a while loop to perform actions until a condition turns from True to False
or from False to True.
DANGER: condition in a while loop may never turn from True to False or from 
False to True. In this case, the while loop will go on forever and will be 
known as an Infinite Loop.

'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

























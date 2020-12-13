# Nested if statements#
# if statements inside if statements

# basic rules of nested if statements
'''
if condition:
    if another_condition:
        print("Do this inner thing")
    else:
        print("Do this inner thing instead")
else:
    print("Do this outer thing")
'''

# Example
height = int(input("What is your height in cm? "))


if height >= 120:
    #print("You can ride the roller coaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("It costs £5, please.")
    elif age >= 12 and age < 18:
        print("It costs £7, please.")
    else:
        print("It costs £12, please.")
else:
    print("Sorry, you have to grow taller before you can com aboard.")















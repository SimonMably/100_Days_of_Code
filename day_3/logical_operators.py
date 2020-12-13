
# Using logical operaters to check multiple conditions in the same if statement
# (or line)

a = 12

# Not using logical operators
if a > 15:
    print("a is > than 15")
else:
    print("a is not > than 15")

if a > 10:
    print("a is > than 10")

# Using logical operators

# and 
if a > 10 and a < 15:
    print("\na is > than 10 and a is < than 15")
else:
    print("\nOne or both conditions are false.")
# With the 'and' logical operator, both conditions must be true for the print
# function to work.

# or 
if a > 10 or a < 15:
    print("\nEither condition 1 is true, or condition 2 is true or both "
          "are true")
# the if statement will be False only when both conditions are false 


# not
if not a < 10:
    print("\nboolean value condition has been reversed")
# if condition is true, not will reverse the outcome and make the condition
# false.

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill += 5
        print(f"Child tickets cost {bill}.")
    elif age >= 12 and age < 18:
        bill += 7
        print(f"Child tickets cost {bill}.")
    elif age >= 18 and age < 45:
        bill += 12
        print(f"Child tickets cost {bill}.")
    elif age >= 45 and age <= 55:
        print("Everything is okay. Have a free ride on us!")
    elif age >= 56:
        bill += 12
        print(f"Child tickets cost {bill}.")

    wants_photo = input("Do you want a photo? y or n: ")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can com aboard.")



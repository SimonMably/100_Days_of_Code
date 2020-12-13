
# checking to see if 1 condition is true:
'''
if condition_1:
    do A
elif condition_2:
    do B
else:
    do C

Only one of these conditions will be true (usually its the first condition that
is considered true thst will be used. The rest of the conditions in the 
if-elif-else that come after will be ignored).
'''

# checking to see if multiple conditions are true
'''
if condition_1:
    do A
if condition_2:
    do B
if condition_3:
    do C
'''
# eg 
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print(f"Child tickets cost {bill}.")
    elif age >= 12 and age < 18:
        bill = 7
        print(f"Child tickets cost {bill}.")
    else:
        bill = 12
        print(f"Child tickets cost {bill}.")

    wants_photo = input("Do you want a photo? y or n: ")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can com aboard.")



































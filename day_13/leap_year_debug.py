
# input() function returns a TypeError because its string datatype doesn't 
# match all of the integer datatypes within the nested if-else statements.
#* year = input("Which year do you want to check?")

# Solve by wrapping input() function within an int() function to convert its 
# datatype to an integer.
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


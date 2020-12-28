
#! Problem 1: "FizzBuzz" gets printed at every 3rd and 5th number.
#* Solution: replace the 'or' in the condition with 'and' to print FizzBuzz
#*           every 15th number.

#! Problem 2: The program contains 3 seperate if statements. Along with the 
#!            if statement below, "FizzBuzz", "Fizz", "Buzz" AND each number
#!            (except the number 5) gets printed.
#* Solution: Turn seperate if/if-else statements into a if-elif-elif-else block
#*           so each condition works in conjunction with each other.

#! Problem 3: within the print() statement, 'number' is wrapped in 
#!            square brackets. This means that each number gets printed 
#!            as a list.
#* Solution: get rid of the square brackets and the numbers will be 
#*           printed as normal.

for number in range(1, 101):
    # if number % 3 == 0 or number % 5 == 0:
    if number % 3 == 0 and number % 5 == 0:
         print("FizzBuzz")
    # if number % 3 == 0:
    elif number % 3 == 0:
        print("Fizz")
    # if number % 5 == 0:
    elif number % 5 == 0:
        print("Buzz")
    else:
        #print([number])
        print(number)


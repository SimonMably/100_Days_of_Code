
# Iterating / looping over a range of numbers:
# for number in range(0, 11):
#     print(number)

# The range function will not give provide the second given number
# eg. for number in range(0, 10): will loop up to 10 but won't include 10. If 
# we absolutely need to include the number 10 in the range(), the we will need
# to have to set the range as range(0, 11).

# By default, the for loop will loop through range() funcion 1 number at a 
# time (or 1 step at a time). We can increase the step size by adding another
# number as a parameter to the range function.
for number in range(0, 11, 3):
    print(number)
# This for loop iterates through a range of numbers of 0 - 11, three numbers
# at a time.


# Looping through a range of 0 - 100 and adding each number to each other
total = 0
for number in range(0, 101):
    total += number
print(total)




























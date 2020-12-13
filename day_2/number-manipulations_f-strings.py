# Rounding numbers:

# If we print 8 / 3, we would get a float number:
print(8 / 3)  # = 2.6666666666666665

# But if convert the same equation into an integer, the point and everything
# after would get chopped off:
print(int(8 / 3))  # = 2

# If we wanted to round the result properly, we would need to use the 
# round() function:
print(round(8 / 3))  # = 3

# If we wanted to round to a particular decimal place instead to the nearest
# whole number, we could it like:
print(round(8 / 3, 2))  # = 
# The number after the comma refers to the number of decimal places.

# -----------------------------------------------------------------------------

# Floor Division

print(8 // 3)  # This is the same as print(int(8 / 3))

# -----------------------------------------------------------------------------

# Continuing Calculations

# We can store a calulation in a variable, and then perform further calculations
# upon that variable.
print("")
# eg.
result = 4 / 2
result /= 2
print(result)  # = 1.0

# -----------------------------------------------------------------------------

# Manipulating data in variables
# Adding/subtracting/etc numbers to a variable (like scores, eg.)

score = 0

# User scores a point
score = score + 1
# or to use the shorthand
score =+ 1
# Can also use:
    # score -= 1
    # score *= 1
    # score /= 1

# -----------------------------------------------------------------------------

# f-strings

# With f-strings, we can place different data types within strings without
# having to convert data types.

# eg.
score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}. your height is {height}, it is {isWinning} that"
       " you're winning.")

# By using f-strings, we cut down on the amount of manual labour regarding 
# putting different data types within strings.





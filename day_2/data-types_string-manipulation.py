# Data Types
# -----------------------------------------------------------------------------

# Strings
"This is a string."
'This is also a string.'
# Anything withn single/double quotes is considered a string, even numbers and
# other characters.

# Integer
123
# Whole numbers are considered integers

# Float
3.14
# Numbers with a decimal are considered as floats.
# Also known as Floating point numbers.

# Boolean
True
False
# A boolean is, simply, either True or False.
# True and False are both keywords that are boolean data types.

# Type function
# type() can be used to display the data type of a given value. eg.:

# ex.1
num_char = len(input("What is your name? "))
print(type(num_char))

# ex.2
num_char = input("What is your name? ")
print(type(num_char))

# The data type for ex.1 is Integer, because a string/input function is being 
        # passed through the len() function.
# The data type for ex.2 is String, because a string is being passed through 
        # the input() function.


# -----------------------------------------------------------------------------
# Type Conversion / Type Casting
# -----------------------------------------------------------------------------

# Type concersion or type casting is where we can change a piece of data from 
# one data type to another data type.

# eg. 
num_char = len(input("What is your name? "))  # The len() function makes this 
                                              # variable an integer

new_num_char = str(num_char)  # The str() function converts the num_char
                              # variable into a string and it goes into a new 
                              # variable.

print("Your name contains " + new_num_char + " characters.")  
# This displays the converted data type in a string.

# Converting other data types

a = 123
print(type(a))  # Will show that 'a' is an integer

a = str(123)
print(type(a))  # Will show that 'a' has been converted into a string.

a = float(123)
print(type(a))  # Will show that 'a' has been converted into a float.

# -----------------------------------------------------------------------------
# Example. retreiving a two digit number and adding both digits together
# using type conversion and subscripting (using index positions).
# Two methods that achieve the same result.

# Method 1:
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Method 2:
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)

print(result)

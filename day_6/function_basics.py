# How to make a function:
'''
def function_name():  # Function Definition
    # Do this
    # Then do this
    # Finally do this

my_function()  # Function Call

'''

# The print() function is a built-in function.
print("Hello")
num_char = len("Hello")  # The len() function is a built-in function as well.
print(num_char)

### Example of a function that I could make myself:

# Functions are defined with the 'def' keyword along with the name of the 
# function followed by open and closed parentheses and a colon. Any indented 
# code immediately following the functions definition will be apart of that 
# function.
def my_function():   
    print("Hello")  # Apart of 'my_function()'
    print("Bye")  # Apart of 'my_function()'

# To use a function, we need to do what's known as calling the function
my_function()
# If a function requires any parameters (or inputs), then they will need to be
# entered within the function calls parentheses. my_function doesn't need any 
# arguements, which mens they can remain blank.

# Functions are useful because it allows us to write a block of code once and 
# then re-use that code as many times as we need to. This also allows us to 
# write less code and makes our code more readable as well.

# -----------------------------------------------------------------------------
# Indentation =================================================================
# -----------------------------------------------------------------------------
'''
In python, indentations are important. Any code that is part of a block of 
code (or code block) will be indented.

Functions, if-elif-else statements and loops will have their own code block. 
First, the function, if (and/or elif and/orelse) statement or loop will be 
defined, and then all of the indented code on the proceeding lines will be 
apart of that function, if (and/or elif and/orelse) statement or loop.

If-elif-else statements / nested if-elif-else statements and loops / nested
loops can be placed in each other and in and functions. This can make 
indentation and code blocks hard to look at and/or tricky to look at.

'''
sky = "clear"
def indentation_example():
    if sky == "clear":
        for cloud in range(0, 4):
            print(cloud)
        else:
            print("blue")
    elif sky == "cloudy":
        print("grey")
    print("Hello")
print("World")

# To create indents, we can either use the tab key or press the spacebar 4 
# times.




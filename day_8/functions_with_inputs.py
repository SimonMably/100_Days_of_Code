# A basic function with 3 print statements.
# def greet():
#     print("Hello!")
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# # A call to the 'greet()' function (executes code in the 'greet()' function).
# greet()

# -----------------------------------------------------------------------------

# A function that allows for input
# We can place parameters (or inputs) within the functions parentheses. These 
# parameters act as variables for the function to work. The name of each
# parameter needs to be relevent in regards to what information is being passed
# to that parameter.
def greet_with_name(name):  # name = parameter
    print(f"Hello! {name}")
    print(f"How do you do, {name}?")
    print("Isn't the weather nice today?")

# Within the parentheses of the function call, we need to place an argument 
# (for each parameter) that acts as the values for the functions parameters. 
# In this case, we are passing a name.
# The argument is the peice of data that will be passed to the parameter.
'''greet_with_name("Simon")'''  # "Simon" = argument

# Parameter = the name of the data being passed into the function.
# Argument = the actual value of the data.
# Some people use both terms interchangebly.

# Also, if a function takes multiple parameters, their argument counter-parts
# should be entered in the function call in the same order.

# -----------------------------------------------------------------------------
# Functions with more than 1 input (multiple parameters and variables)

# Positional Arguments

def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")

print("Positional Argument")
greet_with("Simon", "Brighton")
# Again, the right arguments should be entered in the same order as the 
# parameters they represent. If they have been mixed up, then they will not 
# make sense when they get used. 

# For example
print("\nPositional Argument (arguments in wrong place)")
greet_with("Brighton", "Simon")
# Will print:
# Hello, Brighton!
# What is it like in Simon?

# The 1st argument is assigned to the 1st parameter and the 2nd argument is 
# assigned to the 2nd parameter.
# In Python programming, these are known as positional arguments (there can be
# as many of these positional arguments as we may want or need (as long as 
# there is a matching number of parameters)).

# -----------------------------------------------------------------------------
# keyword Arguments


# Keyword arguments:
# With keyword arguments, we have to state which argument is equal to which 
# parameter inside the function call. This is done to avoid any possible
# mix-ups that may come with posittional arguments.

# -----------------------------------------------------------------------------

# Differences between positional arguments and keyword arguements:
def my_function(a, b, c):
    # Do this with a
    # Do this with b
    # Do this with c
    pass

# Positional arguments
my_function(1, 2, 3)
# The arguments need to be matched up with the right parameters in regards with
# their positions.

# Keyword Arguments
my_function(a=1, b=2, c=3)
my_function(c=3, a=1, b=2)
# Within the function call, each argument has to equal the correct/intended
# parameter to avoid any mix-ups. Also, as long as each arguments is equalled 
# to the correct parameter, it will not matter in which order they are placed
# within the function call.

# Positional and keyword arguments cannot occur in the same function call.

# Positional / Keyword arguments are just different ways of passing data 
# through a function call.

print("\nKeyword Arguments")
greet_with(name="Simon", location="Brighton")
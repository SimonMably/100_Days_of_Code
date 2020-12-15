# Examples of functions:

# 1. Bog standard function
def standard_function():
    pass  # keyword that acts as a placeholder for code
    # Functions act as container for blocks of code that are intended to be 
    # used multiple times within a program (without having to be typed out
    # each time).
        # Do this
        # Then do this
        # Finally do this
# function call

# 2. Functions with inputs
def function_with_inputs(thing1, thing2):  # thing1 and thing2 are inputs
    pass                                   # (or parameters)
    # Do this with 'thing1' and 'thing2'
    # Then this
    # Finally do this

# function_with_inputs(123, 456)  # <--Arguments in parentheses represent the 
                                  # parameters function definition. The 
                                  # arguments get passed into the functions
                                  # parameters, and gets used within the 
                                  # functions code block/body.

# 3. Functions with outputs
def function_with_outputs():
    # We can have inputs with this sort of function, but they are not 
    # required. Inputs and outputs are seperate things. 
    # In the body of the function, we could do a calculation and save it 
    # to a variable. 
    # Once done, we need to use the output keyword 'return' along with 
    # whatever we want the ouput to be.
    # eg:
    # result = 3 * 2
    # return result
    pass
# function_with_outputs()

#! When the return keyword is used, everything thst comes after it is going to 
#! replace where the function was called.

# Converting strings to title case using title()
def format_name():
    # First name
    f_name = input("What is your first name? ")

    # Last Name =
    l_name = input("What is your last name? ")

    formatted_name = f"{f_name} {l_name}".title()
    print(formatted_name)

format_name()

'''# COURSE SOLUTION

def format_name1(f_name, l_name):
    print(f_name.title())
    print(l_name.title())

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    # print(f"{formatted_f_name} {formatted_l_name}")
    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name1("simon", "mably")
print(formatted_string)
'''
# The title() method either;
    # 1) if all letters are lowercase, capitalises the first letter of each 
    #    word in a string
    # or 
    # 2) if all letters are upercase, uncapitalises all letters except the 
    #    first letter of each word in a string.

#! Reminder:
#! When the return keyword is used, everything thst comes after it is going to 
#! replace where the function was called.

###############################################################################
# Docstrings

# Docstrings are strings that are used primarily for documentation purposes. 
# Docstrings can be wrapped in triple-single quotes or triple-double quotes.
# Docstrings should be placed on the first line of; 1) a file(?? maybe), 
# 2) a class or 3) a function. Docstrings should explain the purpose of these 
# 3 things. 

# Docstrings can use more than one line (as apposed to using #) and can be used 
# as a single/multi- lined comment if it isn't assigned to anything (variables
# and such).



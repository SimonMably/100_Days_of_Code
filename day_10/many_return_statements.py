
#* Seeing what will happen if we add more than 1 return statement

def format_name_1(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name_1("simon", "mably"))

# When the computer encounters a line of code with the return keyword, then it
# knows that line is the end of the function. Any line of code that appears
# after the return statement (and still inside the function) will not get 
# executed. 

# Example of a function containing more than 1 return statement
def format_name_2(f_name, l_name):
    if f_name == "" or l_name == "":
        return  # If 'f_name' and 'l_name' are empty return 'None'.
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name_2(input("What is your first name? "),
                    input("What is your last name? ")))

# The return statement can be left empty, but it's better if it wasn't empty.
# For the if statement in the above example, instead of leaving the return
# statement blank, it could return the string "You didn't provide valid inputs".
# This would be a way to indicate to a user that they need to give a valid 
# response or continueing with something that we didn't want them to do in a 
# program. 

##############################################################################

#* The difference between using print() and using the return statement.

#? print()
# When called, the program will write out the characters within the print()
# functions parantheses out ont screen. 
# The print() function should be used when we need a program to show a 
# value/values to people.

#? return
# return is a keyword. When a return statement is reached, Python will stop the
# execution of the current function, sending a value out to where the function
# was called.
# The return function should be used when we want to send a value from one 
# point in a our code to another. We can combine values this way???

#* Using return changes the flow of the program, while print() does not.



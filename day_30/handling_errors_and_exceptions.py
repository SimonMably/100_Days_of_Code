# If a piece of code causes an error or doesn't work, we will receive a
# traceback message telling us what caused the problem, where it was caused
# and a related error type. When this happens, the error stops the program
# and the code that comes after error causing code doesn't run.

# Types of errors:

# - FileNotFoundError
'''
with open("a_file.txt") as file:
    file.read()
'''
# Opening a file that doesn't exist in read mode and trying to read the
# file. This give a FileNotFoundError

# - KeyError
'''
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]
'''
# Receive a KeyError if we try to access a dictionaries key/value when the
# Key doesn't exist or there is a typo in the key name.

# - IndexError
'''
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]
'''
# Trying to access an item in a list at an index that doesn't exist.

# - TypeError
'''
text = "abc"
print(text + 5)
'''
# Trying to mix 2 different data types (eg. adding an integer to a string

# ---------------------------------------------------------------------------- #

# When it comes to errors, we can either do 1 of 2 things:
# 1: Use these errors as an indicators that there is a problem with our code
# and try to fix the problem as and when they arise.

# 2: In a lot of cases, things follow 'Murphy's Law' ('Anything that can go
# wrong will go wrong'). This means that we should plan for these eventualities.

# It is often best to go with the 2nd option where possible. We can plan for
# errors by 'catching Exceptions'.
# By catching Exceptions, we can either fail gracefully or decide to do
# something else instead.

# What the code will look like when dealing with exceptions:
'''
try:
    # Trying some code that might cause an Exception
except:
    # Do this if there was an Exception (if code in try block was unsuccessful)
else:
    # Do this if there was no Exceptions (if code in try block was successful)
finally:
    # Do this no matter what (code here will happen regardless of the outcome.
    # Usually used to clean/tidy things up a the end of some code execution).
'''
# ---------------------------------------------------------------------------- #
# Example of using Exception handling (eg. FileNotFoundError):

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary)
    print(a_dictionary["key"])
except FileNotFoundError:
    # ^ Don't leave the except statement empty ^. We need to catch specific
    # Exceptions.
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    # 1. We can use multiple except statements to catch multiple Exceptions
    #    (one except statement per possible Exception);
    # 2. We can store whatever causes an Exception in a variable and then use
    #    it to let us know what it is (in this case, a nonexistent dictionary
    #    key will be stored in the variable 'error_message')
    print(f"That key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    # The finally block might not happen very often, but can be handy in
    # certain situations. eg. if we need to close a file.
    file.close()
    print("File was closed.")

# Note: If Exceptions do occur, whatever code in the other except blocks or
# else block won't get executed.

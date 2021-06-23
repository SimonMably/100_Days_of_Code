
# Instructions:
# Create a `logging_decorator()` which is going to log the name of the function that was called,
# the arguments it was given and finally the returned output.

# HINT 1: You can use `function.__name__` to get the name of the function.
# HINT 2: You'll need to use `*args`

# Expected Output:
# You called a_function(1, 2, 3)
# It returned: 6

def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(*args)}")
    return wrapper


# Use logging_decorator()
@logging_decorator
def a_function(*args):
    """Adds *args together and returns the total."""
    return sum(args)


@logging_decorator
def b_function(*args):
    """Multiplies *args with following *arg and returns the total"""
    # eg. if *args = 2, 5, 7, 10
    # 2 * 5 * 7 * 10
    # the for loop calculate the total
    num = 1
    for arg in args:
        num *= arg
    return num


@logging_decorator
def c_function(*args):
    """Checks the type of each argument, appends the answer into a list and returns
    the list."""
    arg_type = []
    for arg in args:
        if type(arg) == int:
            answer = "Integer"
            arg_type.append(answer)
        elif type(arg) == bool:
            answer = "Boolean"
            arg_type.append(answer)
        elif type(arg) == str:
            answer = "String"
            arg_type.append(answer)
    return arg_type


a_function(5, 15, 45, 85)
b_function(2, 2, 2, 99, 10)
c_function(1, "hello", False, "Python", 2005)

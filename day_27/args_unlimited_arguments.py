
# *args: Many Positional Arguments

# *args = any number/unlimited number of Positional Arguments
# Any term can technically be used, but by convention, most people use *args
# (we don't need to use it if we don't want to).


# We can create functions that can potentially take an unlimited amount
# Example, A function that returns the sum of 2 numbers (n1 and n2):
def add_1(n1, n2):
    return n1 + n2


print(add_1(n1=5, n2=3))


# To use the example above, if we wanted to add more than 2 numbers together
# without having to type out (for example) 'n1 + n2 + n3 + n4', we can use
# '*args' as an argument, which will allow us to define an unlimited amount
# of arguments.

# Instead of the function above, we can use *args as an (unlimited use?) 
# argument to add as many numbers as we want/need:

def add_2(*args):
    for n in args:
        print(n)


add_2("\n", 6, 9, 5, True, 7, 3, "Hello", [])


# Challenge: Modify the 'add' function to take an unlimited number of
# arguments. Use a loop to sum all the arguments inside the function.

def add(*args):
    # *args will be presented as a tuple, so we can access its indices:
    print(args[0])

    total = 0
    for n in args:
        total += n
    return total


print(add(3, 5, 6, 99))

# It's important to know that *args will be presented as a tuple.

# 'Unlimited Arguments' using '*args' is also known as 'Unlimited Positional
# Arguments'.

# See 'playground.py' for all course related code for *args and **kwargs

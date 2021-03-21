
# Keyword Argument:

def my_function_1(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    print(a, b, c)


my_function_1(c=3, a=1, b=2)

# With keyword arguments, we can assign a value to an argument in a function
# call and in any order (like above).
# But, if arguments have the same values all of the time (if not most of the
# time), then we can give these arguments default values. We can give
# arguments default values when we declare the function (the function
# definition). eg:


def my_function_2(a=1, b=2, c=3):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    print(a, b, c)


my_function_2()

# When we do this, we don't need to give any inputs in the function call.
# But, if we want to change the value of an argument, we can do that in the
# function call, which will overrule the default value.eg:

my_function_2(b=5)

# Also, since these arguments have default values, if we wanted to change
# their values, we could need to change the values of the arguments that
# need changing, not all of them.

# Something to note:
#  - Function arguments with default values are optional.
#    Input for these arguments should happen only if we need to change the value
#    from the default to whatever value we needed.
#  - Function arguments without default values are mandatory. Input for these
#    values are required.

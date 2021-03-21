
# **kwargs = any number/unlimited number of Keyword Arguments

# **kwargs uses 2 asterisks (**), as opposed to *args, which uses 1 asterisk.

def calculate(**kwargs):
    print(kwargs)
    # We can loop through **kwargs (in dictionary form
    for key, value in kwargs.items():
        print(key)
        print(value)
    # We can also access the value via the dictionary key
    print(kwargs["add"])
    print(kwargs["multiply"])


# Where *args are presented in a tuple, **kwargs are
# presented in a dictionary.
# This function call will print will print the **kwargs in a dictionary.
# 'add' and 'multiply' will be Keys, since they are keywords, and '3' and '5'
# will be there values respectively.
calculate(add=3, multiply=5)


# Using regular arguments with **kwargs
def calculate_2(n, **kwargs):
    print(kwargs)
    # Adds "add" **kwarg to n and then multiplies n by "multiply" **kwarg
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# 2 == n
calculate_2(2, add=3, multiply=5)


# Using **kwargs in a class
class Car:

    def __init__(self, **kwarg):
        # The problem with accessing the **kwargs dictionary in this manner
        # (eg. kwargs["make"]) is that this method actually requires some
        # input for the dictionary key (this is a problem because **kwargs
        # are supposed to be optional). If we miss a **kwarg, we will get a
        # KeyError traceback because using kwargs["make"], for example,
        # Python is is expecting the name of a dictionary key name,
        # essentially making the **kwargs mandatory. This is not good for
        # **kwargs as they're supposed to be optional.
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]

        # Using the .get() function instead:
        self.make = kwarg.get("make")
        self.model = kwarg.get("model")
        # The benefit of using the get() function is that, if a key doesn't
        # exist in the **kwargs dictionary, then .get() will return 'None'.
        # With the get() function, we will not get any errors.


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make, my_car.model)

my_other_car = Car(make="Ford")
print(my_other_car.make, my_other_car.model)

# See 'playground.py' for all course related code for *args and **kwargs

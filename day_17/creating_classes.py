
# Create a class with the 'class' keyword along with the name of the class.
# Naming conventions suggest a class name should be capitalised. If a class
# name contains multiple words, then there should be no spaces in between each
# word and the first letter of each word should be capitalised. This is
# called PascalCase.

class Users:
    # In Python, classes (and functions and loops) can't be empty. If a class
    # is empty, Python will give an error. To get around an error, we can use
    # the 'pass' keyword if we're not ready to place any code in a class. The
    # pass keyword is used as a placeholder.
    pass


# Creating an object
user_1 = Users()

# * An attribute is a variable that is associated with an object
# Creating attributes for a class by using the dot (.) notation. We can
# create as many attributes as we like with this method.

user_1.id = "001"
user_1.username = "simon"

print(user_1.username)
print(user_1.id)

# Creating attributes like this for each object can be prone to error (we can
# make typos or change the name of an attribute in another object, etc). It
# can also be time consuming and take up a lot of lines of code.

# We can make this simpler by using a constructor. A constructor is apart of
# the blueprint that allows us to specify what should happen when an object
# is being constructed. This is also know, in programming, as initialising (
# or initializing) an object. When an object is being initialised, we can set
# variables or counters to their starting values.
# In Python, we can create a constructor by using the init function.
# Example:
'''
def __init__(self):
    # Initialise attributes
'''
# This __init__ function (or method) will be added to a class (it will be the
# first function to be added). Inside the __init__ function is where
# attributes and starting values are initialised.
# * The __init__ function is going to be called everytime we create a new
# * object from the same class that the __init__ function is placed in.
# Attributes are the things that the object will have. For example, for a car
# class can have an attribute for the number of seats and another attribute
# for the colour.
'''What the init function would look like:
class Car:
    def __init__(self, seats, colour):
        self.seats = seats
        self.colour = colour

# Creating a car object with 5 seats and the object itself is red
my_car = Car(5, "red")
'''
# self represents the object that's being created. Then we can as many
# parameters as we like or need. Those parameters are going to be passed in
# when an object gets constructed from a class. And once we receive that
# data, then we can use it to set the objects attribute.
# * Setting attributes in an init function is the same as:
#   my_car.seats = 5
#   my_car.colour = "red"

# * Using an init function to set attributes is a lot quicker and less error
# * prone when we're creating a lot of objects that need all the same
# * attributes.


# Example of an init function in a class:
class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        # Usually, by convention, the parameter name and the attribute name are
        # the same, but technically we can call the attribute anything that
        # we want.

    # The 'self' parameter will be used as the first parameter so, when the
    # method is called, it will know the object that called it.
    def follow(self, user):
        user.followers += 1
        self.following += 1


# We have to pass the attributes in the parentheses. The order of the
# attributes should match the order of the parameters (if they don't match,
# the data won't make much sense).
user_1 = User("001", "simon")
user_2 = User("002", "angela")

print(user_1.id, user_1.username)
print(user_2.id, user_2.username)

# When we add parameters to a constructor to a class, we have to provide data
# for those parameter when creating an object for that class.

# Sometimes, when we're are creating attributes for a class, we may want an
# attribute with a default value. It doesn't always make sense to initialise
# all attributes when creating an object.
# For example, we could be programming an Instagram type app. Each user would
# have an an id and a username (both would be initialised in the constructor).
# Each user would also have followers/a follower count (this wouldn't need to
# be initialised in the constructor but will appear in the constructor as a
# default value (initialised attributes appear as a parameter in the init
# function parentheses, uninitialised attributes, like default values,
# do not)).

print(user_1.followers)

# ! Methods
# * Methods are functions that are associated with an object.

# Example of a method:
'''
class Car:
    def enter_race_mode():
        self.seats = 2
'''
# Also see 'following' method above

# Using the follow() method for user 1 to follow user 2
user_1.follow(user_2)
print()
print(f"user_1 Followers: {user_1.followers}")
print(f"user_1 Following: {user_1.following}")
print(f"user_2 Followers: {user_2.followers}")
print(f"user_2 Following: {user_2.following}")























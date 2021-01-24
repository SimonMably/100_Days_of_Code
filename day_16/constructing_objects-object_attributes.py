"""Using the module Turtle Graphics as an example to construct objects. Also,
learn about modules."""

# ! Constructing Objects

# * imports everything from module
# import turtle

# * imports everything from module
# from turtle import *

# * imports specific things from module
from turtle import Turtle, Screen

import another_module

# accesses and prints 'another_variable' from another_module.py
# print(another_module.another_variable)
# * Will be doing pretty much the same thing with the turtle module as I did
# * with another_variable/another_module.py

# Accessing the Turtle() class from the turtle module. The turtle on the left
# (with the lowercase t) refers to the module, and the Turtle on the right
# (with the uppercase T and the open & closed parentheses) refers to the
# Turtle() class within the turtle module. We can save this into an actual
# object that we get to name (like using it as a value in a variable).

# A turtle object called 'timmy'
timmy = Turtle()
# Because we placed 'from turtle import Turtle' at the top of the file (instead
# of 'import turtle'), we can just reference the Turtle() class (instead of
# typing 'turtle.Turtle()'.

print(timmy)
# At this stage, this prints '<turtle.Turtle object at # 0x027DE4F0>'

# ! Object Attributes
###############################################################################
# * Example - accessing an attribute:
# * car.speed

# * 'car' is an object and 'speed' is the attribute (attributes are essentially
# * variables), which represents the speed of the car object.
###############################################################################

# * Screen() represents the window in which the turtle (the object timmy)
# * will show.
my_screen = Screen()
# Tapping into some of the properties of Screen()
print(my_screen.canvheight)  # Prints 300 onto screen and shows a window briefly

# ! Object Methods

# Methods are functions associated with objects (functions within classes).
# Examples:
# def move():
#     speed = 60
#
# def stop():
#     speed = 0

# The shape() method changes the shape of an object. In this case, it changes
# the shape of the timmy object into a turtle (NOTE: this method needs to be
# place before the 'exitonClick()' method to work)
timmy.shape("turtle")

# The forward() method makes an object move forward by a specified amount (as
# an argument)
timmy.forward(100)

# Using turtles color() method to change the colour of the timmy object.
timmy.color("blue", "magenta")
# The color() method requires 1 or 2 arguments (colour names as strings). If 1
# is given, then the object will be the stated colour. If 2 arguments are
# given, then the outline of the object will be the stated colour of the
# first argument and the the rest of the object will be the stated colour of
# the second argument.

# * Calling/accessing a method example:
# * car.stop()
# 'car' refers to the object, 'stop()' refers to the method.

# The exitonClick() method from turtle graphics' Screen() class keeps the
# turtle graphics screen on the computer screen until a mouse button is
# clicked anywhere on the turtle graphics screen. (The little arrow in the
# middle of the screen is the turtle object (called timmy))
my_screen.exitonclick()



from turtle import Turtle, Screen
import random

# Turtle object
tim = Turtle()

# notes:
#   To know, or figure out, what kind of things the turtle module (or any other
#   module or package) can do, we can go to the modules documentation
#   (docs for the turtle module: https://docs.python.org/3/library/turtle.html)

# Changes the shape of turtle object to a turtle
# tim.shape("turtle")

# notes:
#   Ideally, we should read through a modules documentation before using it.
#   However, that's not always possible. Often, we'll need the help of other
#   people/programmers. We can get that help on websites like StackOverflow
#   (the most popular site for programmers). We can also search for answers
#   on google, which may give us more relevant answers on StackOverflow than
#   if we went to search for the same answers directly on StackOverflow.

'''
# Changes the colour of the turtle object
tim.color("red")

# Moving turtle object 100 pixels
tim.forward(100)

# Turning turtle object right 90 degrees
tim.right(90)

# notes:
#   Uses Screen from turtle module and keep open until click on window
#   All turtle related stuff must be kept above these 2 lines of code.
#   Recommended to keep at bottom of file.
'''
# Changes the colour of the turtle object to red and the border to blue
#tim.color("blue", "red")


screen = Screen()
screen.exitonclick()

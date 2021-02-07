import turtle as t
import random

# Using tuples to generate random RGB colours
example_tuple = (1, 2, 3)

# prints entire tuple
print(example_tuple)

# prints specific item in tuple (by index positions)
print(example_tuple[1])

# Trying to change a tuple (like this or in any way) will return a TypeError
# example_tuple[2] = 7

# The parentheses are not necessary, but make the tuple more readable.
# Tuples are like list, except:
# - tuples use parentheses instead of square brackets and;
# - tuples cannot be changed (list can be changed). Tuples are 'Immutable'.

# Times to use tuples: creating a colour scheme for a website or
# application, creating/using a list containing constant information/data
# that should not change.

# If, for whatever reason, we want to change data inside a tuple, we can
# convert it into a list:
list(example_tuple)

#############################################################################
# Using RGB colours

# RGB (red, green, blue) colours is a way of using a combination of red,
# blue and green to reproduce a broad array of colours. We can utilise rgb
# within a tuple that contains 3 numbers. The 1st number represents the
# colour red. The 2nd color represents green. The 3rd colour represent blue.
# Each number can range from 0 - 255. A mix of different number will produce
# different colours
'''Examples of Colours:
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)
Grey = (127, 127, 127)
White = (255, 255, 255)
Yellow = (0, 255, 255)
Aqua (or light blue) = (255, 255, 0)
Purple = (255, 0, 255)
Pink = (255, 0, 127
'''
# Example RGB colour picker:
# https://www.w3schools.com/colors/colors_rgb.asp

# Generating random RGB colours with the turtle module
tim = t.Turtle()
tim.pen(pensize=5, speed=500)
t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_colour = (r, g, b)
    return rand_colour


directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random_colour())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()

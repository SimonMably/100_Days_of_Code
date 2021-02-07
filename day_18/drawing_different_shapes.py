from turtle import Turtle, Screen
import random

tim = Turtle()

# Challenge 3: Draw a triangle, square, pentagon, hexagon, heptagon, octagon,
# nonagon and a decagon:
# My solution:
triangle = Turtle()
triangle.color("blue")
# 360 / 3 = 120
for _ in range(3):
    triangle.forward(100)
    triangle.right(120)

square = Turtle()
square.color("green")
# 360 / 4 = 90
for _ in range(4):
    square.forward(100)
    square.right(90)

pentagon = Turtle()
pentagon.color("brown")
# 360 / 5 = 72
for _ in range(5):
    pentagon.forward(100)
    pentagon.right(72)

hexagon = Turtle()
hexagon.color("red")
# 360 / 6 = 60
for _ in range(6):
    hexagon.forward(100)
    hexagon.right(60)

heptagon = Turtle()
heptagon.color("sienna")
# 360 / 7 = 51.4285714286
for _ in range(7):
    heptagon.forward(100)
    heptagon.right(51.4285714286)

octagon = Turtle()
octagon.color("magenta")
# 360 / 8 = 45
for _ in range(8):
    octagon.forward(100)
    octagon.right(45)

nonagon = Turtle()
nonagon.color("black")
# 360 / 9 = 40
for _ in range(9):
    nonagon.forward(100)
    nonagon.right(40)

decagon = Turtle()
decagon.color("chocolate")
# 360 / 10 = 36
for _ in range(10):
    decagon.forward(100)
    decagon.right(36)
'''

# Course Solution:
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)


# shape_side_n = value (depending where abouts in range()
# 11 = stop number, will not be included.
for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)
'''

screen = Screen()
screen.exitonclick()

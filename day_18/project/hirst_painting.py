from turtle import Turtle, Screen, colormode
import random
# import colorgram

# Retrieved colours from an image using the module 'colorgram'
# colours = colorgram.extract("image.jpg", 35)
# rgb_colours = []
# for colour in colours:
#     red = colour.rgb[0]
#     green = colour.rgb[1]
#     blue = colour.rgb[2]
#     rgb_colours.append((red, green, blue))
# print(rgb_colours)

colour_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (224, 141, 62),
               (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68),
               (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86),
               (137, 132, 74), (48, 155, 195), (183, 191, 202), (58, 47, 41),
               (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48),
               (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187),
               (223, 178, 168), (54, 45, 52), (179, 199, 184), (133, 41, 39),
               (76, 63, 49), (38, 79, 82)]

spot = Turtle()
spot.speed("fastest")
# Makes Turtle object invisible
spot.hideturtle()

# To deal with RGB colour values of between 0 and 255
colormode(255)

# So pen does not draw a line from default position to set position at new
# y and x positions
spot.penup()

x_position = -210.0
y_position = 240.0
spot.setposition(x_position, y_position)


def line_of_dots():
    for _ in range(10):
        spot.dot(20, random.choice(colour_list))
        spot.forward(50)


for _ in range(10):
    line_of_dots()
    y_position -= 50.0
    spot.setposition(x_position, y_position)


screen = Screen()
screen.exitonclick()

'''
# Course Solution:

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()
color_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (224, 141, 62),
              (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68),
              (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86),
              (137, 132, 74), (48, 155, 195), (183, 191, 202), (58, 47, 41),
              (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48),
              (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187),
              (223, 178, 168), (54, 45, 52), (179, 199, 184), (133, 41, 39),
              (76, 63, 49), (38, 79, 82)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
'''

from turtle import Turtle, Screen, colormode
import random

# Challenge 5: Drawing s spirograph

tim = Turtle()
tim.speed(100)
colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_colour = (r, g, b)
    return rand_colour


heading = 7

for _ in range(51):
    tim.color(random_colour())
    tim.circle(100)
    tim.setheading(heading)
    heading += 7

screen = Screen()
screen.exitonclick()

'''# Course Solution

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

'''

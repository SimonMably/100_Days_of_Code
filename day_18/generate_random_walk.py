from turtle import Turtle, Screen
import random

# What is a Random Walk:
# https://en.wikipedia.org/wiki/Random_walk

tim = Turtle()
# Set the tim objects pen size (drawing width) and movement speed
tim.pen(pensize=5, speed=500)

colours = ["blue", "green", "red", "brown", "purple", "black", "coral", "gold",
           "gray", "cyan"]
# North, East, South, West
directions = [0, 90, 180, 270]

for _ in range(75):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))

# while True:
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     print(tim.pos())
#     if tim.pos() > (350, 350) or tim.pos() < (-350, -350):
#         break
#     # elif tim.pos() > (350, -350) or tim.pos() < (350, -350):
#     #     break


# h = tim.pos()
# tim.speed(500)
# tim.fd(1)
#
# while tim.pos() != h:
#     tim.color(random.choice(colours))
#     tim.lt(random.randint(1, 360))
#     tim.fd(random.randint(1, 5))


screen = Screen()
screen.screensize(500, 500)
screen.exitonclick()

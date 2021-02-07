from turtle import Turtle, Screen

tim = Turtle()

# Challenge 1:
# Using turtle object to draw a square on the screen
# My Solution
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)

# Use a for loop to do the above to avoid coding on so many lines
# Course Solution
for _ in range(4):
    tim.forward(100)
    tim.right(90)


screen = Screen()
screen.exitonclick()

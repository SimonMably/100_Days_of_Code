from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.forward(10)


screen = Screen()

# Event listener
screen.listen()
# We do not need to add the parentheses when using a function as a parameter.
# Basically, uses a function as an input (this is known as Higher Order
# Functions).
# (fun = function, key = keyboard key (for key bindings)).
screen.onkey(fun=move_forward, key="Up")
screen.exitonclick()

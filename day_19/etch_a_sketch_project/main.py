from turtle import Turtle, Screen

# todo 1: Use keys to move: W = forwards, S = backwards, A = counter-clockwise,
#         D = clockwise, C = clear screen (and place turtle object in center
#         of screen)

pen = Turtle()
screen = Screen()


def move_forward():
    """Used in conjunction with the Turtle modules event listener/key
    presses. Binds 'W' key to move turtle forwards."""
    pen.forward(10)


def move_backwards():
    """Used in conjunction with the Turtle modules event listener/key
    presses. Binds 'S' key to move turtle backwards."""
    pen.backward(10)


def turn_right():
    """Used in conjunction with the Turtle modules event listener/key
    presses. Binds 'W' key to move turtle to the right."""
    # My solution
    pen.right(10)

    # Course solution
    # new_heading = pen.heading() + 10
    # pen.setheading(new_heading)


def turn_left():
    """Used in conjunction with the Turtle modules event listener/key
    presses. Binds 'W' key to move turtle to the left."""
    # My solution
    pen.left(10)

    # Course solution
    # new_heading = pen.heading() - 10
    # pen.setheading(new_heading)


def clear_screen():
    """Clears Turtle screen of existing drawings and returns Turtle to center
    of screen."""
    # Both methods will clear the screen and reset turtle to default position
    # pen.reset()
    screen.resetscreen()

    # Course solution
    # pen.clear()
    # pen.penup()
    # pen.home()
    # pen.pendown()


# Event listeners for movement keys
screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_forward, key="W")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_backwards, key="S")
screen.onkey(fun=turn_right, key="a")
screen.onkey(fun=turn_right, key="A")
screen.onkey(fun=turn_left, key="d")
screen.onkey(fun=turn_left, key="D")

# Event key to clear the screen
screen.onkey(fun=clear_screen, key="c")
screen.onkey(fun=clear_screen, key="C")

screen.exitonclick()


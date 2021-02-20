from turtle import Turtle

R_STARTING_POSITION = (350, 0)
L_STARTING_POSITION = (-350, 0)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    """Class that creates user-controlled paddles. Size, shape, movement."""

    def __init__(self, starting_position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.starting_position = starting_position
        self.goto(self.starting_position)

    def up(self):
        """Sets paddle heading/movement towards top of screen. Corresponds
        with 'up' arrow keybinding defined in main file."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        """Sets paddle heading/movement towards bottom of screen. Corresponds
        with 'down' arrow keybinding defined in main file."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

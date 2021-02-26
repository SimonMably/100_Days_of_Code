from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):
    """Manages player controlled turtle object appearance and behaviour."""

    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(UP)

    def move_up(self):
        """Allows player to move turtle object up the screen. Corresponds
        with the up arrow keybinding defined in main file."""
        # self.forward()  # will also work
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reached_finish_line(self):
        """When player reaches the finishing line at y position 280."""
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)

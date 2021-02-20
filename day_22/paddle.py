from turtle import Turtle

R_STARTING_POSITION = (350, 0)
L_STARTING_POSITION = (-350, 0)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle:
    """Class that creates user-controlled paddles. Size, shape, movement."""
    def __init__(self, starting_positions):
        # super().__init__()  # If Paddle() inherits from Turtle()
        self.paddles = []
        self.starting_positions = starting_positions
        self.create_paddles()

    def create_paddles(self):
        """Creates user controlled paddle."""
        # We can also get Paddle class to inherit from Turtle class and also
        # remove 'paddle = Turtle()' and move everything else here to the
        # __init__
        paddle = Turtle()
        paddle.color("white")
        paddle.shape("square")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.goto(self.starting_positions)
        self.paddles.append(paddle)

    def up(self):
        """Sets paddle heading/movement towards top of screen. Corresponds
        with 'up' arrow keybinding defined in main file."""
        for paddle in self.paddles:
            new_y = paddle.ycor() + 20
            paddle.goto(paddle.xcor(), new_y)

    def down(self):
        """Sets paddle heading/movement towards bottom of screen. Corresponds
        with 'down' arrow keybinding defined in main file."""
        for paddle in self.paddles:
            new_y = paddle.ycor() - 20
            paddle.goto(paddle.xcor(), new_y)

from turtle import Turtle
import time


class Ball(Turtle):
    """Represents the ball that players use to score against each other."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move_ball(self):
        """Moves ball towards top-right corner of the screen."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Ball bounces when it collides with either top or bottom edges of
        screen."""
        # self.y_move has been set to 10 in init method. code below is the
        # same as subtracting 10
        self.y_move *= -1

    def bounce_x(self):
        """Ball bounces when it collides with a player controlled paddle."""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_ball_position(self):
        """Resets ball to starting position, ball moves in opposite direction
        towards paddle that didn't miss."""
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()

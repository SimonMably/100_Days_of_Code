from turtle import Turtle
import random


class Ball:
    """Represents the ball that players use to score against each other."""

    def __init__(self):
        # Ball() class could also inherit from Turtle() class.
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        # self.ball.speed("slowest")
        # Make list of random numbers between -300 - 300 and get y_move and
        # x_move to choose from list
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        """Moves ball towards top-right corner of the screen."""
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def bounce(self):
        """Ball bounces when it collides with either top or bottom edges of
        screen."""
        # self.y_move has been set to 10 in init method. code below is the
        # same as subtracting 10
        self.y_move *= -1

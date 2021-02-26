from turtle import Turtle
import random


class Food(Turtle):
    """Acts as in-game food for snake. Each piece of food gives snake
    additional segments."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # Stretches shape along its length and width/defines size of shape
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("LimeGreen")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Generates food at random location on screen at start of game and
        after each time snake collides with food."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

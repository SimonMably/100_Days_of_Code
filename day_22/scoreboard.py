from turtle import Turtle


class Scoreboard(Turtle):
    """Displays scores for both the right and left paddles"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scores()

    def update_scores(self):
        """Updates scores of both paddles on screen."""
        self.goto(-100, 220)
        self.write(self.left_score, align="center",
                   font=("Comic Sans MS", 50, "normal"))
        self.goto(100, 220)
        self.write(self.right_score, align="center",
                   font=("Comic Sans MS", 50, "normal"))

    def left_point(self):
        """Player controlling the left paddle receives point."""
        self.clear()
        self.left_score += 1
        self.update_scores()

    def right_point(self):
        """Player controlling the right paddle receives point."""
        self.clear()
        self.right_score += 1
        self.update_scores()

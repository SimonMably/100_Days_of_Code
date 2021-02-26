from turtle import Turtle

TEXT_Y_POSITION = 275
ALIGNMENT = "center"
FONT = ("Ebrima", 12, "normal")


class Scoreboard(Turtle):
    """Keeps track of players score and displays score on screen."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=0, y=TEXT_Y_POSITION)
        self.hideturtle()
        self.color("white")
        self.display_score()

    def display_score(self):
        """Displays players score at the top of the screen. Clears previous
        score from screen and displays new score every time player snake
        eats food."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases players score each time player controlled snake gets
        food."""
        self.score += 1
        self.clear()
        # Updating score works without calling:
        # self.display_score()

    def game_over(self):
        """Enacts Game Over when snake collides with itself or a wall."""
        self.goto(0, 0)
        self.write(f"GAME OVER!!", align=ALIGNMENT, font=FONT)

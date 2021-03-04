from turtle import Turtle

TEXT_Y_POSITION = 275
ALIGNMENT = "center"
FONT = ("Courier", 13, "normal")


class Scoreboard(Turtle):
    """Keeps track of players score and displays score on screen."""

    def __init__(self):
        super().__init__()
        # 'data.txt' is used to store the games high score
        self.file = open("data.txt")
        self.high_score = self.file.read()
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
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", 
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases players score each time player controlled snake gets
        food."""
        self.score += 1

    def reset_score(self):
        """Checks if score is greater than the high score. If true, set score to
        as high score. Then resets score to 0."""
        if self.score > int(self.high_score):
            # Opens 'data.txt', writes high score
            self.file = open("data.txt", "w")
            self.file.write(str(self.score))
            self.file.close()

        self.file = open("data.txt")
        self.high_score = self.file.read()
        self.score = 0
        # self.display_score()

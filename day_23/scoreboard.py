from turtle import Turtle

FONT = ("Courier", 12, "normal")
POSITION = (-250, 280)
GAME_OVER_POSITION = (0, 0)
GAME_OVER_FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    """Displays level number and 'GAME OVER' on screen."""
    # todo: write 'Level: {level_number}' at top left of screen DONE
    # todo: Write 'GAME OVER' when turtle collides with a car DONE

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.display_level()

    def display_level(self):
        """Updates level if player turtle reaches destination."""
        self.goto(POSITION)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        """At each new level of game, clears level from screen, updates to
        new level and redisplay current level to screen."""
        self.level += 1
        self.clear()
        self.display_level()

    def game_over(self):
        """Writes 'GAME OVER' at center of screen."""
        self.clear()
        self.goto(GAME_OVER_POSITION)
        self.color("black")
        self.write(f"GAME OVER\nYou reached {self.level}", align="center",
                   font=GAME_OVER_FONT)

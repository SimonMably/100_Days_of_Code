import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# todo: create player behaviour in Player() class DONE
# todo: create car behavior in CarManager() class DONE/REWORK:regenerate_cars()?
# todo: detect turtle collides with a car in main while loop DONE
# todo: detect when player/turtle reaches other side in main while loop DONE
# todo: add scoreboard and game over sequence in Scoreboard() class DONE

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

# Instances
player = Player()
car_manager = CarManager()
score = Scoreboard()

# Keybindings
screen.listen()
# screen.onkey(player.move_up, "Up")
screen.onkeypress(player.move_up, "Up")
# Use 'screen.onkeypress()' instead if you want to move continuously without
# having to press the up button each tim you want to move (hold down up button)

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Moves cars and regenerates cars if they reach left edge of screen
    car_manager.move_cars()
    car_manager.regenerate_cars()

    # Detect when player turtle reaches finishing line
    if player.ycor() == 280:
        player.reached_finish_line()
        score.increase_level()
        car_manager.increase_car_speed()

    # Detects collision between player turtle and cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen Attributes
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Snake, Food and Scoreboard instances
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Keybindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    # Delay: 0.1 second
    time.sleep(0.1)
    snake.move()
    scoreboard.display_score()

    # Detect collision between Snake and Food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision between snakes head and walls
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290:
        scoreboard.reset_score()
        snake.reset_snake()
    elif snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detects collision between snakes head and snakes tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()

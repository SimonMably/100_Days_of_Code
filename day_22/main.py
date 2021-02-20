from turtle import Screen
import time
from paddle_v2 import Paddle
from ball_v2 import Ball
from scoreboard import Scoreboard

# Screen Attributes
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Instances
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

# Keybindings
screen.listen()
# Paddle on right of screen
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
# Paddle on left of screen
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.up, "W")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(left_paddle.down, "S")

# Main Game Loop
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    # ball == instance of Ball() class
    ball.move_ball()

    # Detects collision between ball and top/bottom edges of screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detects collision between the ball and both paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detects when right paddle misses
    if ball.xcor() > 380:
        ball.reset_ball_position()
        score.left_point()

    # detects when left paddle misses
    if ball.xcor() < -380:
        ball.reset_ball_position()
        score.right_point()

screen.exitonclick()

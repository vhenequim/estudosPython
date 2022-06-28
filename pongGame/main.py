from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pongus")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
paddle_diagonal = 50.99     

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision detection:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddle:
    if ball.xcor() > 320 and ball.distance(r_paddle) < paddle_diagonal or ball.xcor() < -320 and ball.distance(l_paddle) < paddle_diagonal:
        ball.bounce_x()

    # Miss:
    if ball.xcor() > 380:   # Right side
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:  # Left side
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()

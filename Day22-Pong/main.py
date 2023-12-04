from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
x = 0.1

screen.listen()

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update(), time.sleep(x), ball.moving()

    # ball collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(False)

    # ball collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce(True)
        x *= 0.9

    # game loss on side walls
    if ball.xcor() > 380 or ball.xcor() < -380:

        if ball.xcor() > 380:
            scoreboard.l_point()
            scoreboard.update_scoreboard()
            x = 0.1

        elif ball.xcor() < -380:
            scoreboard.r_point()
            scoreboard.update_scoreboard()
            x = 0.1

        ball.reset_position()

    # paddle collision with walls
    if l_paddle.ycor() > 250:
        l_paddle.goto(l_paddle.xcor(), 250)
    elif l_paddle.ycor() < -250:
        l_paddle.goto(l_paddle.xcor(), -250)

    if r_paddle.ycor() > 250:
        r_paddle.goto(r_paddle.xcor(), 250)
    elif r_paddle.ycor() < -250:
        r_paddle.goto(r_paddle.xcor(), -250)

screen.mainloop()


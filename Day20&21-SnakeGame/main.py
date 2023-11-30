from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update(), time.sleep(.1), snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh(), scoreboard.increase_score(), snake.grow()

    # Detect collision with wall
    if (snake.head.xcor() > 290 or snake.head.xcor() < -295
            or snake.head.ycor() > 295 or snake.head.ycor() < -290
            or any(snake.head.distance(segment) < 10 for segment in snake.segments[1:-1])):
        game_is_on = False
        scoreboard.game_over()

screen.mainloop()

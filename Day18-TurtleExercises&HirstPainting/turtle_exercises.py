import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def make_square(mover):
    x = 0
    mover.forward(100)
    while x < 3:
        mover.right(90)
        mover.forward(100)
        x += 1


def make_dashed_line(mover, distance):
    x = 0
    while x < distance:
        mover.forward(10)
        mover.penup()
        mover.forward(10)
        mover.pendown()
        x += 1


def draw_shapes(mover, sides):
    for _ in range(sides):
        angle = 360 / sides
        mover.forward(100)
        mover.right(angle)


def random_walk(mover):
    mover.pensize(15)
    mover.speed("fast")
    for _ in range(200):
        mover.forward(30)
        direction = random.choice(directions)
        mover.setheading(direction)
        mover.color(random_color())


def draw_spirograph(mover, size_of_gap):
    mover.speed("fastest")
    mover.shape("circle")
    for _ in range(int(360 / size_of_gap)):
        mover.circle(100)
        mover.color(random_color())
        mover.setheading(mover.heading() + size_of_gap)


tim = Turtle()
tim.shape("turtle")
tim.color("green")

# make_square(tim)

# make_dashed_line(tim, 20)

# for shape_side_n in range(3, 11):
#     draw_shapes(tim, shape_side_n)
#     tim.color(random_color())

# random_walk(tim)

# draw_spirograph(tim, 1)

screen = Screen()
screen.exitonclick()

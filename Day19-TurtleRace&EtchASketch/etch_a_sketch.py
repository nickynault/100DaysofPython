from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(move_forwards, "w")
screen.onkeypress(turn_left, "a")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(turn_right, "d")
screen.onkey(clear, "c")

screen.mainloop()  # keeps window open

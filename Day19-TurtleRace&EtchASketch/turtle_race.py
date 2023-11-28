from turtle import Turtle, Screen
import random

tim = Turtle()
tom = Turtle()
benny = Turtle()
billy = Turtle()
jen = Turtle()
wendy = Turtle()

screen = Screen()
screen.setup(width=700, height=360)

turtles = [tim, tom, benny, billy, jen, wendy]
colors = ["green", "blue", "purple", "brown", "black", "pink"]
speeds = ["slowest", "slow", "normal", "fast", "fastest"]


def initialize_turtles():

    for index, turtle in enumerate(turtles):
        new_color = random.choice(colors)
        turtle.color(new_color)
        colors.remove(new_color)
        turtle.shape("turtle")
        turtle.shapesize(2)
        turtle.penup()
        turtle.goto(-250, -120 + index * 50)

    draw_finish_line()


def draw_finish_line():
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.goto(230, -180)
    finish_line.pendown()
    finish_line.goto(230, 180)
    finish_line.hideturtle()


def betting():
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    return user_bet.lower() if user_bet else None


def race():
    winner = None

    for turtle in turtles:
        turtle.speed(random.choice(speeds))

    while max(turtle.xcor() for turtle in turtles) < 230:
        for turtle in turtles:
            turtle.forward(random.randint(1, 5))
        screen.update()

        # Check for winner
        winner = max(turtles, key=lambda turt: turtle.xcor())

    return winner


def display_winner(win):
    turtle_winner = Turtle()
    turtle_winner.hideturtle()
    turtle_winner.penup()
    turtle_winner.goto(0, 0)
    turtle_winner.write(f"The winner is the {win.color()[0]} turtle!", align="center", font=("Arial", 16, "normal"))

    if bet is not None:
        if bet == win.color()[0]:
            result = "Congratulations! Your bet was right!"
        else:
            result = "Sorry, your bet was wrong.\n Better luck next time."

        turtle_result = Turtle()
        turtle_result.hideturtle()
        turtle_result.penup()
        turtle_result.goto(0, -50)
        turtle_result.write(result, align="center", font=("Arial", 14, "normal"))


initialize_turtles()
bet = betting()
the_winner = race()
display_winner(the_winner)

screen.mainloop()

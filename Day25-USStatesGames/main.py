import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

# this finds the coordinates needed in the CSV, just click on anything and get an x and a y.
# def get_mouse_coordinates(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_coordinates)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 Correct",
                                   prompt="What is another state's name?").title()

    if user_answer == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        wrong_answers = pandas.DataFrame(missing_states)
        wrong_answers.to_csv("what_you_missed.csv")
        exit(0)

    if user_answer in states:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("black")
        state_data = data[data.state == user_answer]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(user_answer)
    else:
        exit(0)


screen.mainloop()


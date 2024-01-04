# main.py Flashcard app

from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("data/french_words.csv")
    to_learn = og_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def random_word():
    global current_card, flip_timer

    app.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = app.after(3000, func=switch_cards)


def switch_cards():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learns.csv", index=False)

    random_word()


app = Tk()
app.title("Flashcards")
app.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = app.after(3000, func=switch_cards)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas.card_front = card_front_img
canvas.card_back = card_back_img

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

unknown_button_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_img, highlightthickness=0, bd=0, command=random_word)
unknown_button.image = unknown_button_img
unknown_button.grid(row=1, column=0)

check_button_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_button_img, highlightthickness=0, bd=0, command=is_known)
check_button.image = check_button_img
check_button.grid(row=1, column=1)

random_word()

app.mainloop()

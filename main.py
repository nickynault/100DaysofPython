# main.py Flashcard app

from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def random_word():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


app = Tk()
app.title("Flashcards")
app.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas.card_front = card_front

canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

unknown_button_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_img, highlightthickness=0, bd=0, command=random_word)
unknown_button.image = unknown_button_img
unknown_button.grid(row=1, column=0)

check_button_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_button_img, highlightthickness=0, bd=0, command=random_word)
check_button.image = check_button_img
check_button.grid(row=1, column=1)

random_word()

app.mainloop()

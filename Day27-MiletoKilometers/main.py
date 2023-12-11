from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=500, height=300)

miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 24, "bold"))
equal_label.grid(column=0, row=1)

answer_label = Label(text="0", font=("Arial", 24, "bold"))
answer_label.grid(column=1, row=1)

kilo_label = Label(text="Km", font=("Arial", 24, "bold"))
kilo_label.grid(column=2, row=1)


def convert():
    miles = int(entry.get())
    kilometers = miles * 1.609
    answer = str(kilometers)
    answer_label["text"] = answer


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

entry = Entry(width=10)
entry.grid(column=1, row=0)

window.mainloop()

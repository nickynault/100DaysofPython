from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ("Arial", 14, "normal")


# ---------------------------------------------SAVING DATA--------------------------------------------------------#
def save():
    global is_ok
    website = web_entry.get()
    email = user_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 and len(password) == 0:
        messagebox.showinfo(title="Error", message="One or more boxes have not been filled in. "
                                                   "\nPlease don't leave them blank!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")

    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------------------------GENERATE PASSWORDS----------------------------------------------------#
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)  # copies generated password to your clipboard


# ---------------------------------------------PASSWORD SEARCH-------------------------------------------------------#
def find_password():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Result Found", message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="No Result Found", message="Sorry, no details for this website exist.")
    

# ---------------------------------------------UI SETUP--------------------------------------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

tag1 = Label(text="Website:", font=FONT)
tag1.grid(row=1, column=0)
tag2 = Label(text="Email/Username:", font=FONT)
tag2.grid(row=2, column=0)
tag3 = Label(text="Password:", font=FONT)
tag3.grid(row=3, column=0)

web_entry = Entry(width=40)
web_entry.grid(row=1, column=1)
web_entry.focus()
user_entry = Entry(width=35)
user_entry.grid(row=2, column=1)
user_entry.insert(0, "user@gmail.com")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

pass_button = Button(text="Generate Password", font=FONT, command=gen_pass)
pass_button.grid(row=3, column=2)
add_button = Button(text="Add", font=FONT, width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", font=FONT, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()

from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_pwd():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "@", "#", "$", "%", "&", "(", ")", "*", "+", ]
    """Generates a random password"""

    # nr_letters = randint(8, 10)
    # nr_symbols = randint(2, 4)
    # nr_numbers = randint(2, 4)

    pwd_letters = [choice(letters) for _ in range(randint(8, 10))]
    pwd_num = [choice(number) for _ in range(randint(2, 4))]
    pwd_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = pwd_letters + pwd_symbol + pwd_num

    # shuffles the password so it appears random
    shuffle(password_list)
    # ---------------------------- SAVE PASSWORD ------------------------------- #
    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char
    password_input.insert(0, password)
    pyperclip.copy(password)


def save_data():
    site = website_input.get()
    email = email_input.get()
    pwd = password_input.get()

    if len(site) == 0 or len(pwd == 0):
        messagebox.showinfo(
            title="Error", message="Please make sure all fields are filled")
    else:
        okay = messagebox.askokcancel(
            title=site, message=f"These are details entered:\nEmail: {email}\nPassword: {pwd}\nIs it correct?")

        if okay:
            with open("data.txt", mode="a") as file:
                file.write(f"{site} | {email} | {pwd}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


# initializing window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="pink")

# getting the logo image
logo = PhotoImage(file="logo.png")
# loading the logo
canvas = Canvas(width=200, height=200, bg="pink", highlightthickness=0)
# creating the image based on the x and y
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# creating the labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# creaing the inputs
website_input = Entry(width=39)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_input = Entry(width=39)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END, "@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# buttons
generate_btn = Button(text="Generate Password", command=gen_pwd)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=33, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)

# keeping the window open at all times
window.mainloop()

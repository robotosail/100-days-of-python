import json
from signal import NSIG
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# generating a password
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
    # copying password to clipboard
    pyperclip.copy(password)


# saving the data
def save_data():
    site = website_input.get()
    email = email_input.get()
    pwd = password_input.get()
    # format of the data
    new_json_data = {
        site:
        {
            "email": email,
            "password": pwd
        }
    }

    # checking to make sure has no lenght of 0
    if len(site) == 0 or len(pwd) == 0:
        messagebox.showinfo(
            title="Error", message="Please make sure all fields are filled")
    else:
        # confirming that the data is correct
        okay = messagebox.askokcancel(
            title=site, message=f"These are details entered:\nEmail: {email}\nPassword: {pwd}\nIs it correct?")

        if okay:
            # checking if the data.json file already exists
            try:
                # reading json data file
                with open("data.json", mode="r") as file:
                    # reading old data
                    data = json.load(file)
            # catching error by creating the file
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    # writing data into json file
                    json.dump(new_json_data, file, indent=4)
            else:
                # updating the json data
                data.update(new_json_data)

                with open("data.json", mode="w") as file:
                    # writing data into json file
                    json.dump(data, file, indent=4)
            finally:
                # empyting user input field.
                website_input.delete(0, END)
                password_input.delete(0, END)


# search for data
def search_data():
    # getting the site to be searched
    site = website_input.get()
    # catching errors
    try:
        # opening the json file
        with open("data.json") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(
            title="Error", message="You don't have any saved passwords, save a password by clicking the add button")

    else:
        # checking if the seached site matches any of the data
        if site in data:
            # if so get the key with email and password
            email = data[site]["email"]
            password = data[site]["password"]
            messagebox.showinfo(
                title=site, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"You don't have any saved passwords, under the site {site}")

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
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry(width=39)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(END, "@gmail.com")
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# buttons
generate_btn = Button(text="Generate Password",
                      command=gen_pwd)
generate_btn.grid(column=2, row=3)
# sticky = "EW",
search_btn = Button(text="Search", width=10, command=search_data)
search_btn.grid(column=2, row=1)

add_btn = Button(text="Add", width=33, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)

# keeping the window open at all times
window.mainloop()

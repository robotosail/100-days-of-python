import pandas
from tkinter import *
import random

current_card = None
to_learn = None

# converting the data to a dictionary
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("data/french_words.csv")
    to_learn = og_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# triggered when the x button is clicked
def next_card():
    """Goes to the next card"""
    # gaining access to the global variables
    global current_card, flip_timer
    # canceling the 3 sec timer
    window.after_cancel(flip_timer)
    # creating a new random card from the cards to be learnt
    current_card = random.choice(to_learn)
    # current_card["French"]
    # changing the canvas configurations like the text
    canvas.itemconfig(card_title, text="French", fill="green")
    canvas.itemconfig(card_word, text=current_card["French"], fill="green")
    canvas.itemconfig(card_background, image=card_front_img)
    # reseting the 3 sec timer that flips the card
    flip_timer = window.after(3000, func=flip_card)


# is triggered every 3 seconds
def flip_card():
    """Filps the cards over"""
    # getting access to the global variable
    global current_card
    # Updating the ui - like the text
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# triggered when the check mark button is clicked
def is_known():
    # removing the cards that are known by getting the current card
    to_learn.remove(current_card)
    # writing the words to be learnt to a csv file
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    # # for debugging
    # print(current_card)
    # calling the next_card function
    next_card()


BACKGROUND_COLOR = "#B1DDC6"
# init window
window = Tk()
window.title("Flashy")  # -- title of window
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# initially calls the flip card function
flip_timer = window.after(3000, func=flip_card)

# images for the front and back cards
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526)
# getting rid of the image border
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# adding the front and back images to the screen
card_background = canvas.create_image((400, 263), image=card_front_img)
card_title = canvas.create_text(
    400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="Word", font=("Arial", 60, "bold"))

# setting the position of the canvas grid
canvas.grid(row=0, column=0, columnspan=2)

# images for the check and x mark
cross_img = PhotoImage(file="images/wrong.png")
check_img = PhotoImage(file="images/right.png")

# buttons
unkown_btn = Button(image=cross_img, highlightthickness=0, command=next_card)
unkown_btn.grid(row=1, column=0)
known_btn = Button(image=check_img, highlightthickness=0, command=is_known)
known_btn.grid(row=1, column=1)
next_card()

# keep window open
window.mainloop()

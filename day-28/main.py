import math
import time
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# allows reset of the timer


def reset_timer():
    window.after_cancel(timer)
    # changing the title from work back to timer
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"00:00")
    global reps
    reps = 0
    check_mark.config(text="")


def start_timer():
    global reps
    # incrementing the reps every time function is called
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # checking if the reps is divisible by 8
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    # checking if the reps is divisible by 2: if so it is time for break
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

    # or

    # for i in range(1, 8):
    #     # if the number i is divisible by 2 then take a break
    #     if i % 2 == 0:
    #         # calling countdown function
    #         count_down(short_break_sec)
    #     else:
    #         count_down(work_sec)


def count_down(count):
    global timer
    # getting the minutes: divide the count by 60 and floor it
    minutes = math.floor(count / 60)
    # calculating the seconds: by dividing the count and getting the remainder
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    # updating the screen
    canvas.itemconfig(timer_text, text=f"{minutes}:{sec}")
    if count > 0:
        # window.after is similar to setInterval
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✅"
        check_mark.config(text=marks)


    # ---------------------------- UI SETUP ------------------------------- #
    # initializing the window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

# creating a canvas to load the image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=("Comic", 18, "bold"))
canvas.grid(column=1, row=1)

# creating a tile text
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW,
                    font=("Comic", 40, "bold"))
title_label.grid(column=1, row=0)

# creating start and reset button
start_btn = Button(text="start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

# creating and adding check mark
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)


window.mainloop()

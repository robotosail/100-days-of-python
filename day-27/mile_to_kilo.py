from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")


# initializing window screen
window = Tk()
window.title("Miles to Kilo Converter")
# setting the padding of the window
window.config(padx=20, pady=20)

# creating an input box for user input
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# creating labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calculate_btn = Button(text="calculate", command=miles_to_km)
calculate_btn.grid(column=1, row=2)

window.mainloop()

import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States game")

image = "blank_states_img.gif"
# getting each of the states from the csv file
data = pandas.read_csv("50_states.csv")
# turning the data into a list
all_states = data.state.to_list()
# adding a new shape to the list of turtle shapes
screen.addshape(image)
# turning the turtles shape to the image
turtle.shape(image)

# holds states guessed
guessed_states = []
on = True
# holds states not guessed

# while loop continues until all 50 states are guessed correctly
while len(guessed_states) < 50:
    guess = screen.textinput(
        f"{len(guessed_states)}/50 states correct", "Name a state").title()

    if guess == "Exit":
        # using list comprehension ot shorten code
        states_to_learn = [
            state for state in all_states if state not in guessed_states]

        # for state in all_states:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)

        data_to_learn = pandas.DataFrame(states_to_learn)
        data_to_learn.to_csv("states_to_learn.csv")
        break
# checking if the guess is in the states list
    if guess in all_states:
        guessed_states.append()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # gets the row of the guessed state both the x and the y
        # state_data = data[data.state == guess]
        # getting the index position of the guess from the all state list then using it to find the corresponding x and y position
        # t.goto(int(state_data.x), int(state_data.y))
        t.goto(data["x"][all_states.index(guess)],
               data["y"][all_states.index(guess)])
        t.write(guess, align="center")


# keeps the screen open even after program ended
# turtle.mainloop()

# getting the coordinates of the clicked position
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

import random
import turtle

raceon = False
screen = turtle.Screen()
# increasing the size of the screen
screen.setup(width=500, height=400)
# creating a popup
bet = screen.textinput(title="Make a bet",
                       prompt="Which turtle do you think will win the race?").lower()
turtles = []

# creating a list of y position for the turtle
y_position = [-60, -30, 0, 30, 60, 90]
# list ot hold the colors
colors = ["red", "orange", "yellow", "blue", "green", "coral"]
# looping six times to create six turtles
for t_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[t_index])
    new_turtle.penup()
    # setting the initial position of the turtles
    new_turtle.setpos(x=-230, y=y_position[t_index])
    # appending the newly created turtles to the turtle array
    turtles.append(new_turtle)

if bet:
    raceon = True
while raceon:
    # looping through the turtles list and assigining it random distance speed
    for t in turtles:
        random_distance = random.randint(0, 10)
        t.forward(random_distance)
        # check if one of the turtles have reached end of the screen
        if t.xcor() > 230:
            raceon = False
            winner = t.pencolor()
            # comparing user bet with the winner color
            if winner == bet:
                print(f"You won! The winner was the {winner} turtle")
            else:
                print(f"You lose! The winner was the {winner} turtle")

screen.exitonclick()

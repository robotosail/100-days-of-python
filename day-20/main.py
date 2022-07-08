import turtle
import random
import time

colors = ["red", "yellow", "green", "blue"]

screen = turtle.Screen()
# setting up the screen
screen.setup(width=600, height=600)
# setting the screen color
screen.bgcolor("grey")
# setting the title of the screen
screen.title("Snake Game")
# turning of the animation
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
# creating 3 turtle body
for position in starting_positions:
    new_segment = turtle.Turtle(shape="square")
    new_segment.color("limegreen")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


on = True

while on:
    screen.update()
    for segment in segments:
        segment.fd(20)
        # adds a 1 second delay to the program
        time.sleep(1)

screen.exitonclick()

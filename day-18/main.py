import random
import turtle as t

turtle = t.Turtle()
# changing the color mode of the turtle module and not the object
t.colormode(255)

# getting hold of the screen
screen = t.Screen()

directions = [0, 90, 180, 270]


# creates random colors
def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb = (red, green, blue)
    return rgb


for i in range(250):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))
    # set the thickness of the pen
    turtle.pensize(10)
    turtle.speed(10)

screen.exitonclick()

# # drawing shapes from triangle to decagon
# def draw(number, angle):
#     # draws a triangle
#     for i in range(number):
#         # changes the color of the pen
#         turtle.fillcolor(choice(colors))
#         turtle.fd(100)
#         turtle.right(angle/(number))

# for i in range(3, 11):
#     # changes the fill color
#     # turtle.color(choice(colors))
#     # turtle.begin_fill()
#     # draw(i, 360)
#     # turtle.end_fill()
#     turtle.color(choice(colors))
#     draw(i, 360)

# make the screen close only when clicked

# # drawing a square using loop
# for i in range(4):
#     t.fd(100)
#     t.rt(90)

# # drawing dashed lines 50 times
# for i in range(50):
#     # moving forward 10 stepss
#     t.fd(10)
#     # pulling the pen up - you can use penup(), pu(), or up()
#     t.pu()
#     t.fd(10)
#     # pulling the pen down - you can use pendown(), pd(), or down()
#     t.pd()

# colors = ["green", "red", "coral", "orange",
#   "blue", "pink", "yellow", "aquamarine"]

# Basic import
# import t
# t = turtle.Turtle()

# importing the t module
# imports a specific method or class from the module
# from t import Turtle, Screen
# t = Turtle()
# screen = Screen()

# turtle.shape("t")
# turtle.color("red")
# turtle.fd(100)
# # turns right by certain degrees
# turtle.rt(90)

# # drawing a square using loop
# for i in range(4):
#     turtle.fd(100)
#     turtle.rt(90)
# screen.exitonclick()
# imports everything from the module

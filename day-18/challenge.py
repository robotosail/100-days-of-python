import turtle as t
import random

my_turtle = t.Turtle()
screen = t.Screen()

t.colormode(255)
# creates random colors


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb = (red, green, blue)
    return rgb


# setting the turtles speed to be fast
my_turtle.speed("fastest")


# draws a spirograph and stops after limit is reached
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        # making the turtles color random
        my_turtle.color(random_color())
        # drawing a circle
        my_turtle.circle(50)
        # changing the heading direction or the turn angle: by getting the previous turn angle and increasing by the size of gap
        my_turtle.seth(my_turtle.heading() + size_of_gap)
        # increasing the turn angle


draw_spirograph(12)
screen.exitonclick()

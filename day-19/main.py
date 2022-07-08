# -----EventListeners in turtle module--------#
import turtle

t = turtle.Turtle()
screen = turtle.Screen()


def move_fowards():
    t.fd(10)


# screen listens for events
screen.listen()
# space pressed run move_forwards
screen.onkey(key="space", fun=move_fowards)
screen.exitonclick()

# higher order functions are functions that can work with other function
# def calculator(func):
# func()

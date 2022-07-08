import turtle

t = turtle.Turtle()
screen = turtle.Screen()
steps = 10


def forwards():
    t.forward(steps)


def backward():
    t.back(steps)


def right():
    t.rt(steps)


def left():
    t.lt(steps)


def reset():
    t.reset()


screen.listen()
screen.onkey(fun=forwards, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=left, key="a")
screen.onkey(fun=right, key="d")
screen.onkey(fun=reset, key="c")
screen.exitonclick()

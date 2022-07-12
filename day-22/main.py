
from turtle import Screen, Turtle
import paddle

t = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game!")
screen.tracer(0)

# creating both paddles
r_paddle = paddle.Paddle((350, 0))
left_paddle = paddle.Paddle((-350, 0))

# listening for key clicks
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

on = True
while on:
    # updating the screen
    screen.update()

screen.exitonclick()

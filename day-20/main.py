import turtle
from snake import Snake
import random
import time
import food

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

snake = Snake()
food = food.Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

on = True
# updating the screen on every movement
while on:
    screen.update()
    # adds a 1 second delay to the program
    time.sleep(0.1)
    snake.move()
    # segments[0].forward(20)
    # segments[0].left(90)
screen.exitonclick()

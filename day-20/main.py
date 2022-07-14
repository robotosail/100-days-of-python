import turtle
from snake import Snake
import random
import time
import food
import scoreboard

colors = ["red", "yellow", "green", "blue"]

screen = turtle.Screen()
# setting up the screen
screen.setup(width=600, height=600)
# setting the screen color
screen.bgcolor("black")
# setting the title of the screen
screen.title("Snake Game")
# turning of the animation
screen.tracer(0)

snake = Snake()
food = food.Food()
score_board = scoreboard.ScoreBoard()

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
    # detect collision with food
    # if the snake head is withing 15 pixels of the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increaseScore()

    # detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score_board.reset()
        snake.reset()

    # detect collision with tail
    for body in snake.segments[1:]:
        if snake.head.distance(body) < 10:
            score_board.reset()
            snake.reset()
screen.exitonclick()

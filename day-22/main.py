import time
from turtle import Screen, Turtle
import paddle
import ball
import scoreboard

t = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game!")
screen.tracer(0)

# creating both paddles
r_paddle = paddle.Paddle((380, 0))
l_paddle = paddle.Paddle((-390, 0))

# creating the ball
ball = ball.Ball()

# score board
score = scoreboard.ScoreBoard()

# listening for key clicks
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

on = True
while on:
    # updating the screen
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -310:
        ball.bounceX()

    # detect when right
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_addscore()
    # left paddle miss the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_addscore()

    score.updateScore()

screen.exitonclick()

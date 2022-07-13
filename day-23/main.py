import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, "Up")

cars = []
amount = 20

for i in range(amount):
    car = CarManager()
    cars.append(car)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 290:
        player.resetposition()
        for car in cars:
            car.incrspeed = True
    for car in cars:
        car.move()
        # if car.xcor() < -310:
        #     car.resetPos()

screen.exitonclick()

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.createCar()
    car.move()
    # detect collision with turtle
    for c in car.cars:
        if c.distance(player) < 35:
            game_is_on = False
    if player.finish():
        player.reset_pos()
        car.level_up()

screen.exitonclick()

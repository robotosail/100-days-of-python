from random import choice, randint
import turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def createCar(self):
        random_chance = randint(1, 6)

        if random_chance == 1:

            # setting the shape of the car
            new_car = turtle.Turtle("square")
            new_car.shapesize(1, 2)
            # raising the pen up
            new_car.penup()
            # randomly picking a color from the list of colors
            new_car.color(choice(COLORS))
            # setting a random y position
            rand_y = randint(-250, 250)
            # getting the car to go to the random y position
            new_car.goto(300, rand_y)
            # appending the car to the cars list
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            # making the car move
            car.backward(self.carspeed)

    def level_up(self):
        self.carspeed += MOVE_INCREMENT

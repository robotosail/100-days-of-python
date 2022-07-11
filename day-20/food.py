import turtle
import random
# getting inheritance of the turtle class


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        # changing the default look of the turtle to circle
        self.shape("circle")
        # putting the pen up
        self.penup()
        # changing the shape of the turtle to a 10 by 10
        self.shapesize(0.5, 0.5)
        # changing the turtles color
        self.color("green")
        # setting the speed to be the fastest
        self.speed(0)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

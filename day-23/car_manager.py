from random import choice, randint
import turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 4)
        self.color(choice(COLORS))
        self.penup()
        self.incrspeed = False
        self.goto(randint(-270, 270), randint(-270, 270))

    def move(self):
        if self.incrspeed == True:
            newx = self.xcor() - MOVE_INCREMENT
            self.goto(newx, self.ycor())
        else:
            newx = self.xcor() - STARTING_MOVE_DISTANCE
            self.goto(newx, self.ycor())
        if self.xcor() < -330:
            self.goto(330, self.ycor())
            self.resetPos()

    def resetPos(self):
        self.goto(self.xcor(), randint(-270, 270))

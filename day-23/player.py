import turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)

    def move(self):
        newy = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), newy)

    def resetposition(self):

        self.goto(STARTING_POSITION)

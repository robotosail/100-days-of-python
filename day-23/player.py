import turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        # setting the shape of the turtle
        self.shape("turtle")
        # putting the pen up
        self.penup()
        # setting heading of the turtle to face north
        self.seth(90)
        # moving the pen's position to the starting position
        self.reset_pos()

    def move(self):
        # increasing the y coordinate of the turtle
        newy = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), newy)

    def finish(self):
        # reseting the position of the turtle
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_pos(self):
        self.goto(STARTING_POSITION)

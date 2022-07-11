import turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
# snake speed
SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        # creating 3 turtle body
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        # looping the starting postion list
        for position in STARTING_POSITION:
            # creating a new turtle object with a square shape and a color of limegreen
            new_segment = turtle.Turtle(shape="square")
            new_segment.color("limegreen")
            # putting the pen up
            new_segment.penup()
            # make it go to a position
            new_segment.goto(position)
            # appending the new object to the segment list
            self.segments.append(new_segment)

    def move(self):
        # looping backwards through the segments
        for segment in range(len(self.segments) - 1, 0, -1):
            # getting the x and y coordinates of the body before it and moving to the new position
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(SPEED)

    def up(self):
        # check if the snake is already going down if not let it go up
        if self.head.heading() != DOWN:
            # changing the heading to go up
            self.head.seth(UP)

    def down(self):
        # check if the snake is already going up if not let it go down

        if self.head.heading() != UP:
            # changing the heading to go down
            self.head.seth(DOWN)

    def left(self):
        # check if the snake is already going right if not let it go left
        if self.head.heading() != RIGHT:
            # changing the heading to go left
            self.head.seth(LEFT)

    def right(self):
        # check if the snake is already going left if not let it go right
        if self.head.heading() != LEFT:
            # changing the heading to go right
            self.head.seth(RIGHT)

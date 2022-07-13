from turtle import Turtle
import turtle


class Paddle(turtle.Turtle):
    """Creates a new paddle for the pong game"""

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 0.3)
        self.penup()
        self.goto(position)

    def move_up(self):
        """move the paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        """move the paddle down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

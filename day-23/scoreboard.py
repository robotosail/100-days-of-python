from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __int__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        # self.goto(-280, 280)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        # self.write(f"Level2: {self.level}", False, align="left", font=FONT)

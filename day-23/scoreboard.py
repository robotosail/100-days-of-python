from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.updateText()

    def incrlvl(self):
        self.level += 1
        self.updateText()

    def updateText(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

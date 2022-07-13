import turtle

ALIGN = "center"
FONT = ("Comic", 40, "normal")


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 240)
        # self.write(fself.l_score, align=ALIGN, font=FONT)
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align=ALIGN, font=FONT)

    def l_addscore(self):
        self.l_score += 1

    def r_addscore(self):
        self.r_score += 1

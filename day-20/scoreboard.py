from re import A
import turtle

ALIGN = "center"
FONT = ("Arial", 24, "bold")


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",
                   align=ALIGN, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"GAME OVER",
                   align=ALIGN, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

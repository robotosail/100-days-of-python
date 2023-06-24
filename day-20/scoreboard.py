import turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # reading the highscore from the file and setting it to a variable
        with open("data.txt") as file:
            contents = int(file.read())
            self.high_score = contents
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}",
                   align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            # editing the file that hold the high score and adding the new highscore
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def increaseScore(self):
        self.score += 1
        self.update_scoreboard()

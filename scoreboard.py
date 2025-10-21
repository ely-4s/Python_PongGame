from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score =0
        self.dashline ="|"
        self.r_score =0
        self.update_scoreboard()
        self.goto(0, 200)
        self.write(self.dashline, align="center", font=("Courier", 40, "normal"))


    def update_scoreboard(self):
        self.clear()
        self.goto(0, 200)
        self.write(self.dashline, align="center", font=("Courier", 40, "normal"))
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))


    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
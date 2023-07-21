from turtle import *


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score)
        self.goto(100, 200)
        self.write(self.r_score)

    def l_point(self):
        self.l_score += 1
        self.updatescore()

    def r_point(self):
        self.r_score += 1
        self.updatescore()

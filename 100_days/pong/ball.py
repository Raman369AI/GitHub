from turtle import *


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10

    def mov(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y *= -1

    def bounce_paddle(self):
        self.x *= -1

    def ball_reset(self):
        self.goto(0,0)
        self.bounce_paddle()

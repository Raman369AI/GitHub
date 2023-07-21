from turtle import *

POSITION = [(0, 0), (0, 40), (0, -40)]
class Paddle():

    def __init__(self):
        self.bat=[]

    def body(self):
        for posit in POSITION:
            raman = Turtle("square")
            raman.color("red")
            raman.penup()
            raman.setposition(posit)
            self.bat.append(raman)


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
from random import *

class CarManager(Turtle):

    def __init__(self):
        self.all_cars=[]
        self.carspeed=STARTING_MOVE_DISTANCE

    def create_cars(self):
        chance=randint(1,6)
        if chance==6:
            new_car= Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y=randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.carspeed)

    def level_up(self):
        self.carspeed += MOVE_INCREMENT





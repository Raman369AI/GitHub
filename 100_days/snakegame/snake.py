from turtle import *

POSITION = [(-20, 0), (-40, 0), (0, 0)]


class Snake:

    def __init__(self):
        self.snakes = []
        self.body()
        self.head = self.snakes[0]

    def body(self):
        for tut in POSITION:
            self.add(tut)

    def add(self, tut):
        raman = Turtle("square")
        raman.color("red")
        raman.penup()
        raman.setposition(tut)
        self.snakes.append(raman)

    # the extend adds the snake part to the previous postion but overlaps with the last segment,
    # the magic happens in the move part, which moves according to the preious segment
    def extend(self):
        self.add(self.snakes[-1].position())

    def move(self):
        for no in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[no - 1].xcor()
            new_y = self.snakes[no - 1].ycor()
            self.snakes[no].goto(new_x, new_y)
            print(f"new{new_x}{new_y}")
        self.head.forward(20)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def reset(self):
        for snake in self.snakes:
            snake.goto(800,800)
        self.snakes=[]
        self.body()
        self.head = self.snakes[0]

from turtle import *
import random
from typing import Tuple

# to use RGB mode the Class color mode must be set to 255 , default it is 0.
colormode(255)
vydehi = Turtle()
vydehi.shape("turtle")
vydehi.pensize(2)
vydehi.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    c_l_r =(r,g,b)
    return c_l_r


for i in range(71):
     vydehi.circle(100)
     vydehi.left(5)
     vydehi.pencolor(random_color())


vydehig = Screen()
vydehig.exitonclick()

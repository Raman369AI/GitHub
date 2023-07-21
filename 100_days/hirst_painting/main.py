import turtle
import random
import colorgram
from turtle import *

turtle.colormode(255)
colors = colorgram.extract('image.png', 255)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    r_g_b = (r, g, b)
    rgb_colors.append(r_g_b)
paint = Turtle()
paint.speed(0)
paint.penup()
paint.setheading(225)
paint.forward(300)
paint.setheading(0)
paint.hideturtle()
n=100


for i in range(1,n+1):
    paint.dot(20, random.choice(rgb_colors))
    paint.forward(50)
    if i % 10 == 0 :
        paint.setheading(90)
        paint.forward(50)
        paint.setheading(180)
        paint.forward(500)
        paint.setheading(0)
Screen()
exitonclick()
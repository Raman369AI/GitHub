
from turtle import *
import random
colormode(255)
screen = Screen()
turtles=[]
screen.setup(550,550)
user_bet=screen.textinput("Make your bet",prompt="which turtle will win")

raman=Turtle()
raman.shape("turtle")
raman.penup()
raman.color('red')
raman.setposition(-250,-250)
turtles.append(raman)
vydehi=Turtle()

vydehi.shape("turtle")
vydehi.penup()
vydehi.color('green')
vydehi.setposition(-250,-125)
turtles.append(vydehi)
kronos=Turtle()
kronos.shape("turtle")
kronos.penup()
kronos.color('orange')
kronos.setposition(-250,0)

turtles.append(kronos)
hector=Turtle()
hector.shape("turtle")
hector.penup()
hector.color('purple')
hector.setposition(-250,125)
turtles.append(hector)








is_race_on=False
if user_bet:
    is_race_on = True
while is_race_on:

    for tut in turtles:
        if tut.xcor()>230:
            is_race_on = False
            colour=tut.pencolor()
            if colour == user_bet:
                print(f"the winner is  you, {colour}")
            else:
                print(f"the winner is  not you, {colour}")
        tut.forward(random.randint(0,10))

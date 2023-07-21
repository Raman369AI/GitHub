# Snake CLass-Create the snake body
from turtle import *
import snake
import food
import time
from score import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Vydehi")
screen.tracer(0)
python = snake.Snake()
food = food.Food()
screen.listen()
score = Score()
screen.onkey(python.turn_up, "Up")
screen.onkey(python.turn_down, "Down")
screen.onkey(python.turn_left, "Left")
screen.onkey(python.turn_right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.09)
    python.move()

    if python.head.distance(food) < 15:
        food.refresh()
        python.extend()
        score.increase_score()

    if python.head.xcor() > 280 or python.head.xcor() < -280 or python.head.ycor() > 280 or python.head.ycor() < -280:
        score.reset()
        python.reset()

    for pyths in python.snakes[1:]:
        if python.head.distance(pyths) < 10:
            score.reset()
            python.reset()


screen.exitonclick()

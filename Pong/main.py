from turtle import Screen
from Paddle import Paddle
from Score import Score
from Ball import Ball
import time
screen = Screen()
screen.setup(1200, 1000)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
player_1 = Paddle()
player_1.set_position(480, 90)
player_2 = Paddle()
player_2.set_position(-490, -90)


def up_1():
    player_1.set_direction(1)


def down_1():
    player_1.set_direction(-1)


def stop_1():
    player_1.set_direction(0)


def up_2():
    player_2.set_direction(1)


def down_2():
    player_2.set_direction(-1)


def stop_2():
    player_2.set_direction(0)


screen.onkeypress(up_2, "s")
screen.onkeypress(down_2, "w")
screen.onkeyrelease(stop_2, "w")
screen.onkeyrelease(stop_2, "s")

screen.onkeypress(up_1, "Up")
screen.onkeypress(down_1, "Down")
screen.onkeyrelease(stop_1, "Up")
screen.onkeyrelease(stop_1, "Down")
score = Score()
ball = Ball()

while score.game_is_on:
    player_1.move()
    player_2.move()
    ball.move(score, player_1, player_2)
    score.update_score()
    screen.update()
    time.sleep(0.05)
ball.hideturtle()
screen.update()
screen.exitonclick()

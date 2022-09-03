from turtle import Turtle
from math import fabs


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__("circle")
        self.shapesize(1.5, 1.5)
        self.color("white")
        self.penup()
        self.vx = 10
        self.vy = 15

    def move(self, score, player_1, player_2):
        if fabs(self.ycor()) > 480:
            self.vy *= -1
        if fabs(self.xcor()) > 470:
            if player_1.ycor() - 60 < self.ycor() < player_1.ycor() + 60:
                self.vx *= -1
            elif player_2.ycor() - 60 < self.ycor() < player_2.ycor() + 60:
                self.vx *= -1
            else:
                if self.xcor() > 0:
                    score.score_p2 += 1
                else:
                    score.score_p1 += 1
                self.home()
                self.vx *= -1

        self.goto(self.xcor() + self.vx, self.ycor() + self.vy)

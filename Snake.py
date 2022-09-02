from turtle import Turtle
from Score import Score
from math import fabs

class Snake:
    def __init__(self):
        self.snake = [Turtle("square")]
        self.snake[0].color("white")
        self.snake[0].penup()
        self.snake.append(self.snake[-1].clone())
        self.snake.append(self.snake[-1].clone())
        self.direction = 1
        self.is_a_live = True
        self.score = Score()

    def move_up(self):
        if self.direction != 2:
            self.direction = 0

    def move_down(self):
        if self.direction != 0:
            self.direction = 2

    def move_left(self):
        if self.direction != 1:
            self.direction = 3

    def move_right(self):
        if self.direction != 3:
            self.direction = 1

    def move_snake(self):
        for head in reversed(range(1, len(self.snake))):
            self.snake[head].goto(x=self.snake[head - 1].xcor(), y=self.snake[head - 1].ycor())
        if self.direction == 0:
            self.snake[0].goto(x=self.snake[0].xcor(), y=self.snake[0].ycor() + 20)
        elif self.direction == 1:
            self.snake[0].goto(x=self.snake[0].xcor() + 20, y=self.snake[0].ycor())
        elif self.direction == 2:
            self.snake[0].goto(x=self.snake[0].xcor(), y=self.snake[0].ycor() - 20)
        else:
            self.snake[0].goto(x=self.snake[0].xcor() - 20, y=self.snake[0].ycor())
        if  fabs( self.snake[0].xcor()) > 500 or fabs( self.snake[0].ycor()) > 500:
            self.is_a_live = False
        self.dont_touch_tail()

    def eat(self, food):
        if self.dont_touch_food(food):
            while self.dont_touch_food(food):
                pass
            self.snake.insert(1, self.snake[0].clone())
            self.score.score_up()

    def game_result(self):
        self.score.game_over()

    def dont_touch_tail(self):
        for tail in self.snake[2:]:
            if self.snake[0].xcor() == tail.xcor() and self.snake[0].ycor() == tail.ycor():
                self.is_a_live = False

    def dont_touch_food(self, food):
        if self.snake[0].xcor() == food.xcor() and self.snake[0].ycor() == food.ycor():
            food.change_place()
            return True
        return False

import turtle as t
from Food import Food
from Snake import Snake
import time

wight = 1020  # input("Enter wight : ")
height = 1020  # input("Enter height : ")
screen = t.Screen()
screen.setup(width=int(wight), height=int(height))
screen.bgcolor("black")
screen.title("snake game")
snake = Snake()
food = Food(wight, height)
screen.listen()
screen.onkeypress(snake.move_up, "w")
screen.onkeypress(snake.move_down, "s")
screen.onkeypress(snake.move_right, "d")
screen.onkeypress(snake.move_left, "a")
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_right, "Right")
screen.onkeypress(snake.move_left, "Left")
while snake.is_a_live:
    snake.move_snake()
    snake.eat(food)
    time.sleep(0.1)
snake.game_result()
screen.exitonclick()

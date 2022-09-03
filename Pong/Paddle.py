from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super(Paddle, self).__init__("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.direction = 0

    def set_position(self, x, angle):
        self.left(angle)
        self.goto(x, 0)

    def move(self):
        self.forward(self.direction * 10)

    # number -1 0 1
    def set_direction(self, direction):
        self.direction = direction

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, wight, height):
        super(Food, self).__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.width = int((int(wight) / 2) / 20)
        self.height = int((int(height) / 2) / 20)
        self.change_place()

    def change_place(self):

        self.setposition(random.randint(-self.width, self.width) * 20, random.randint(-self.height, self.height) * 20)

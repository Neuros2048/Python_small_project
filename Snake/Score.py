from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-30, 450)
        self.write_score()

    def write_score(self):
        self.write(f'Score {self.score}', align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def score_up(self):
        self.score += 1
        self.clear()
        self.write_score()
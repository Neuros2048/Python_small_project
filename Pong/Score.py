from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score_p1 = 0
        self.score_p2 = 0
        self.game_is_on = True

    def update_score(self):
        self.clear()
        self.goto(-150, 450)
        self.write_score(self.score_p2)
        self.goto(140, 450)
        self.write_score(self.score_p1)
        if self.score_p1 == 5:
            self.write_end("player 1")
        elif self.score_p2 == 5:
            self.write_end("player 2")

    def write_score(self, score):
        self.write(f'Score {score}', align="center", font=("Arial", 24, "normal"))

    def write_end(self, who):
        self.home()
        self.write(f'The winner is {who}', align="center", font=("Arial", 24, "normal"))
        self.game_is_on = False

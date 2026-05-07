
from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCORE = 1

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.points = 0
        self.update_score()


    def update_score(self):
        self.write(f"Level: {self.points}", False, 'left', FONT)
        self.points += SCORE


    def game_over(self):
        self.home()
        self.write("GAME OVER", False, 'center', FONT)


    def clear_scoreboard(self):
        self.clear()
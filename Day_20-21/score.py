from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.sety(280)
        self.points = 0
        self.high_score = 0
        self.high_score_init()
        self.score = None
        self.update_score()


    def update_score(self):
        """
        Clears the printed score and update the score
        """
        self.clear()
        self.score = f"Score: {self.points} - Highest Score: {self.high_score}"
        self.write(self.score, move=False, align='center', font=('Arial', 11, 'normal'))


    def high_score_init(self):
        with open("highest_score.txt") as highest_score:
            self.high_score = int(highest_score.read())


    def reset_score(self):
        """
        Keeps highest score attained
        """
        with open("highest_score.txt", mode="w") as highest_score:
            highest_score.write(f"{self.high_score}")

        self.points = 0
        self.update_score()

    def increase_score(self):
        self.points += 1
        if self.points > self.high_score:
            self.high_score = self.points
        self.update_score()
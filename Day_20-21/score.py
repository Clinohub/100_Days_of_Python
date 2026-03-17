from turtle import Turtle

class Score(Turtle):

    def __init__(self, points=0):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.sety(280)
        self.points = points
        self.text = 'Score: ' + str(self.points)
        self.write(self.text, move=False, align='center', font=('Arial', 11, 'normal'))

    def game_over(self):
        self.home()
        self.write("GAME OVER", align='center', font=('Arial', 20, 'normal'))

    def clear_sb(self):
        """
        Clears the printed score
        """
        self.clear()


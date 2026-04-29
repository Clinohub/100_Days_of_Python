
from turtle import Turtle
from HEADER import Header

header = Header()

class Score(Turtle):
    padding = header.FONT_SIZE + header.OFFSET

    def __init__(self, left_points=0, right_points=0):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(header.SCREENSIZE_HEIGHT / 2 - self.padding)
        self.left_points = left_points
        self.right_points = right_points
        self.text = str(self.left_points) + "     " + str(self.right_points)
        self.write(self.text, move=False, align='center', font=('Courier', header.FONT_SIZE, 'bold'))


    def adjust_score(self, left = 0, right = 0):
        self.left_points += left
        self.right_points += right


    def clear_Score(self):
        self.clear()
            





            
    
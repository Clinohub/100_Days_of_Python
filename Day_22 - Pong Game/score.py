
from turtle import Turtle

class Score(Turtle):
    padding = 70

    def __init__(self, left_points=0, right_points=0):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(300 - self.padding)
        self.left_points = left_points
        self.right_points = right_points
        self.text = str(self.left_points) + "     " + str(self.right_points)
        self.write(self.text, move=False, align='center', font=('Courier', 50, 'bold'))

    def adjust_score(self, left = 0, right = 0):
        self.left_points += left
        self.right_points += right

    def win(self):
        self.home()
        self.write("YOU WIN", align='center', font=('Arial', 20, 'normal'))


    def lose(self):
        self.home()
        self.write("YOU LOSE", align='center', font=('Arial', 20, 'normal'))


    def clear_Score(self):
        self.clear()


class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.sety(400 * -1)
        self.setheading(90)
        self.net_line()
        
        
    def net_line(self):
        while int(self.ycor()) <= self.limit:
            self.pendown()
            self.pensize(10)
            self.forward(40)
            self.penup()
            self.forward(40)
            





            
    
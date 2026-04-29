
from turtle import Turtle
from HEADER import Header

header = Header()

class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.sety(header.SCREENSIZE_HEIGHT / -2)
        self.setheading(90)
        self.net_line()
        
        
    def net_line(self):
        while self.ycor() <= header.SCREENSIZE_HEIGHT / 2:
            self.pendown()
            self.pensize(10)
            self.forward(40)
            self.penup()
            self.forward(40)

from turtle import Turtle

class Road(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.pensize(5)
        self.start_line()
        self.finish_line()


    def start_line(self):
        self.penup()
        self.goto(300, -255)
        self.pendown()
        self.setx(-300)


    def finish_line(self):
        self.penup()
        self.goto(300, 255)
        self.pendown()
        self.setx(-300)
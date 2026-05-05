
from turtle import Turtle
from main import WIDTH,HEIGHT,OFFSET

class Road(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.start_line()
        self.finish_line()

    def start_line(self):
        self.penup()
        self.goto(WIDTH//2 , HEIGHT//-2 + OFFSET)
        self.pendown()
        self.setx(WIDTH//-2)

    def finish_line(self):
        self.penup()
        self.goto(WIDTH//2, HEIGHT//2 - OFFSET)
        self.pendown()
        self.setx(WIDTH // -2)

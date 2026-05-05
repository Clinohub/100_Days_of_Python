
from turtle import Turtle
from main import HEIGHT,OFFSET

STARTING_POSITION = (0, HEIGHT//-2 + OFFSET)
MOVE_DISTANCE = 10
FINISH_LINE_Y = HEIGHT//2 - OFFSET

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.seth(90)
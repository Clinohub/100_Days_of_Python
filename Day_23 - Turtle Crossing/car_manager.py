
from turtle import Turtle
from main import WIDTH, OFFSET

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=1.0, stretch_len=2.0)
        self.color(COLORS[0])
        self.penup()
        self.goto(WIDTH//2 - OFFSET, 0)
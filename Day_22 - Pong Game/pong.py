
from turtle import Turtle
import random

class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=1.0, stretch_len=1.0, outline=None) # pong ball diameter is 20px
        self.color('white')
        self.penup()
        #self.speed("fastest")

    def move(self):
        self.fd(10)

    def bounce(self):
        # no bounce if pong is almost parallel to paddle
        if self.heading() < 87 and self.heading() > 93 or self.heading < 267 and self.heading() > 273: 
            self.seth(360 - self.heading())

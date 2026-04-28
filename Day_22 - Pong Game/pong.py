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

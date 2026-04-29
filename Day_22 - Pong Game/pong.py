
from turtle import Turtle
from HEADER import Header
import random

header = Header()

class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=1.0, stretch_len=1.0, outline=None) # pong ball diameter is 20px
        self.color('white')
        self.penup()
        self.reset()


    def move(self):
        self.fd(header.PONG_PACE)


    def wall_bounce(self, heading):
        # no bounce if pong is almost parallel to paddle
        if heading >= 0 and heading <= 87: # 0 - 87
            self.seth(360 - heading)

        if heading >= 273 and heading < 360: # 273 - 359
            self.seth(360 - heading)
        
        if heading >= 93 and heading <= 267: # 93 - 267
            self.seth(360 - heading)
             

    def paddle_bounce(self):
        self.seth(180 - self.heading())


    def reset(self, serving = "right"):
        self.home() 
        self.drift = random.randint(header.HIGH_RIGHT_ANGLE * -1, header.HIGH_RIGHT_ANGLE)

        if serving == "right":
            self.seth(self.drift)
        else:
            self.seth(self.drift - 180)
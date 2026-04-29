
from turtle import Turtle
from HEADER import Header

header = Header()

class Paddle(Turtle):
    limit = header.SCREENSIZE_HEIGHT / 2 - header.OFFSET * 2
    
    def __init__(self, starting_pos):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid = 5.0, stretch_len = 1.0, outline = None) # default turtle size is 20px 
        self.penup()
        self.speed("fastest")
        self.setx(starting_pos)

    def move_up(self):
        up = self.ycor()
        if up <= self.limit:
            up += header.PADDLE_PACE
            self.sety(up)

    def move_down(self):
        down = self.ycor()
        if down >= self.limit * -1:
            down -= header.PADDLE_PACE
            self.sety(down)

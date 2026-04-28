
from turtle import Turtle

class Paddle(Turtle):
    
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
        if up <= 250:
            up += 20
            self.sety(up)

    def move_down(self):
        down = self.ycor()
        if down >= -250:
            down -= 20
            self.sety(down)

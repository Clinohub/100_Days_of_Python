from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Places Food at random position
        """
        foodX=random.randint(-280, 280)
        foodY=random.randint(-280, 280)
        self.goto(foodX, foodY)

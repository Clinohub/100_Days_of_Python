# Pong Game: The famous Arcade game

# 100 Days of Code ! Day 22


from turtle import Turtle, Screen
from paddle import Paddle
from pong import Pong
import random
import time 

screen = Screen()

screen.setup(width=800, height=600, startx=None, starty=None)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # Turns off animation

right_paddle = Paddle(380)
left_paddle = Paddle(-380)
pong = Pong()
 

screen.listen()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

pong.seth(random.randint(-36, 36))

while True:
    time.sleep(0.1)
    
    # updates the screen when animation is turned off
    screen.update()
    pong.move()

    # define where the ball bounces of walls
    if pong.ycor() > 290 or pong.ycor() < -290:
        pong.bounce()
        
             
    
    

screen.exitonclick()


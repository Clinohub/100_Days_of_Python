from turtle import Turtle, Screen
from paddle import Paddle
from pong import Pong
import random
import time 

screen = Screen()

screen.setup(width=800, height=600, startx=None, starty=None)
screen.bgcolor("black")
screen.title("Pong: The famous Arcade game")
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

    # define how ball bounces of walls
    if pong.ycor() > 290 or pong.ycor() < -290:
        if pong.heading() != 90 or pong.heading() != 270:
            if pong.heading() > 216 and pong.heading() < 324 or pong.heading() > 36 and pong.heading() < 144:
                bounce = 360 - pong.heading()
                pong.seth(bounce)
        
             
    
    

screen.exitonclick()


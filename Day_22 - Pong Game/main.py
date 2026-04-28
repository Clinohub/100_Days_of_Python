# Pong Game: The famous Arcade game

# 100 Days of Code ! Day 22


from turtle import Turtle, Screen
from paddle import Paddle
from pong import Pong
from score import Score, Net

import time 


screen = Screen()

screen.setup(width=800, height=600, startx=None, starty=None)
screen.bgcolor("black")
screen.title("Pong")

score = Score()

screen.tracer(0) # Turns off animation

right_paddle = Paddle(380)
left_paddle = Paddle(-380)
pong = Pong()


#controls
screen.listen()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


# game variables
adjust_right_score = 0
adjust_left_score = 0
delay_speed = 0.1


#game loop
play = True
while play:
    time.sleep(delay_speed)
    

    # updates the screen when animation is turned off
    screen.update()
    pong.move()


    # define where the ball bounces of walls
    if pong.ycor() > 290 or pong.ycor() < -290:
        pong.wall_bounce(pong.heading())


    # detect collision with paddle
    right_x = abs(pong.xcor() - right_paddle.xcor())
    right_y = abs(pong.ycor() - right_paddle.ycor())

    left_x = abs(pong.xcor() - left_paddle.xcor())
    left_y = abs(pong.ycor() - left_paddle.ycor())

    if right_x <= 20 and right_y <= 60: # bounce on right paddle
        pong.paddle_bounce()
        delay_speed *= 0.9995

    if left_x <= 20 and left_y <= 60: # bounce on left paddle
        pong.paddle_bounce()
        delay_speed *= 0.9995

    
    # ball out of bound
    if pong.xcor() > right_paddle.xcor() + 20:
        adjust_left_score += 1  # point for opponent
        pong.reset("left")

    if pong.xcor() < left_paddle.xcor() - 20:
        adjust_right_score += 1  # point for opponent
        pong.reset("right")    
    
    score.clear_Score()
    score = Score(adjust_left_score, adjust_right_score)
              
    
screen.exitonclick()


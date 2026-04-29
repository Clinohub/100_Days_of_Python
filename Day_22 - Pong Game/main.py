# Pong Game: The famous Arcade game

# 100 Days of Code ! Day 22

import HEADER
from turtle import Screen
from paddle import Paddle
from pong import Pong
from score import Score
from net import Net

import time 

header = HEADER.Header()
screen = Screen()

screen.setup(width=header.SCREENSIZE_WIDTH, height=header.SCREENSIZE_HEIGHT, startx=None, starty=None)
screen.bgcolor("black")
screen.title("Pong")

score = Score()

screen.tracer(0) # Turns off animation

screen_right_limit = header.SCREENSIZE_WIDTH / 2
screen_left_limit = screen_right_limit * -1
screen_ceil = header.SCREENSIZE_HEIGHT / 2
screen_floor = screen_ceil * -1

right_paddle = Paddle(screen_right_limit - header.OFFSET)
left_paddle = Paddle(screen_left_limit + header.OFFSET)
pong = Pong()
net = Net()


#controls
screen.listen()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


# game variables
adjust_right_score = 0
adjust_left_score = 0
delay_speed = header.DELAY_SPEED


#game loop
play = True
while play:
    time.sleep(delay_speed)
    

    # updates the screen when animation is turned off
    screen.update()
    pong.move()


    # define where the ball bounces of walls
    if pong.ycor() >screen_ceil - header.OFFSET/2 or pong.ycor() < screen_floor + header.OFFSET/2:
        pong.wall_bounce(pong.heading())


    # detect collision with paddle
    right_x = abs(pong.xcor() - right_paddle.xcor())
    right_y = abs(pong.ycor() - right_paddle.ycor())

    left_x = abs(pong.xcor() - left_paddle.xcor())
    left_y = abs(pong.ycor() - left_paddle.ycor())

    if right_x <= header.PADDING[0] and right_y <= header.PADDING[1]: # bounce on right paddle
        pong.paddle_bounce()
        delay_speed *= header.SPEED_INCREMENT

    if left_x <= header.PADDING[0] and left_y <= header.PADDING[1]: # bounce on left paddle
        pong.paddle_bounce()
        delay_speed *= header.SPEED_INCREMENT

    
    # ball out of bound
    if pong.xcor() > right_paddle.xcor() + header.OFFSET:
        adjust_left_score += header.POINT  # point for opponent
        pong.reset("right")

    if pong.xcor() < left_paddle.xcor() - header.OFFSET:
        adjust_right_score += header.POINT  # point for opponent
        pong.reset("left")    
    
    score.clear_Score()
    score = Score(adjust_left_score, adjust_right_score)
              
    
screen.exitonclick()


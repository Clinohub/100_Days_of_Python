# Turtle Crossing game ! Capstone Project
# 100 Days of Code ! Day 23

from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

WIDTH, HEIGHT = 600,600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

play = True
while play:
    time.sleep(0.1)
    screen.update()

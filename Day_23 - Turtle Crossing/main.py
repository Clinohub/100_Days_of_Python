# Turtle Crossing game ! Capstone Project
# 100 Days of Code ! Day 23

from turtle import Screen
from player import Player
from car_manager import CarManager
from road import Road
from scoreboard import Scoreboard
import time

# screen setup
screen = Screen()
screen.setup(600, 600)
screen.tracer(0) # turn animation off

player = Player()
road = Road()
car_manager = CarManager()
score = Scoreboard()

# player controls
screen.listen()
screen.onkey(player.cross, "Up")

# game loop initialization
play = True
while play:
    time.sleep(0.1)
    screen.update() # updates screen when animation is off

    car_manager.move_cars()
    car_manager.car_is_past_screen_reset()

    # creates car traffic
    if car_manager.generate_car:
        if car_manager.car_distant():
            car_manager.cars()

    # updates score and speeds up the traffic - increases level
    if player.ycor() > 270:
        score.clear_scoreboard()
        score.update_score()
        player.reset_pos()
        car_manager.speed_up()

    # ends game
    for cars in car_manager.traffic:
        if abs(player.xcor() - cars.xcor()) <= 20 and abs(player.ycor() - cars.ycor()) <= 10:
            score.game_over()
            play = False


screen.exitonclick()
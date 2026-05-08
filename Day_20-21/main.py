# Snake Game
# 100 Days 0f Code ! Day 20-21

from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()

# Defining Screen
screen.setup(width=600, height =600)
screen.bgcolor("wheat")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

# User Controls
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "w")

screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")

screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")

screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect Collision with wall
    wall = (snake.head.xcor(), snake.head.ycor())
    if wall[0] >= 290 or wall[0] <= -290 or wall[1] >= 290 or wall[1] <= -290:
        score.reset_score()
        snake.reset_snake()

    # Detect Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()



screen.exitonclick()
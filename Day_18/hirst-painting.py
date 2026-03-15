# hirst painting iitation
# 100 Days of Code ! Day 18 

import turtle
import random

turtle.colormode(255)

colour_list = [(21, 24, 39), (5, 150, 167), (20, 182, 122), (195, 201, 141), (194, 189, 128), (178, 189, 0), (41, 38, 5), (71, 109, 48), (38, 38, 38), (0, 95, 158), (139, 147, 164), (232, 125, 13), (189, 1, 1), (246, 204, 126), (255, 201, 0), (245, 224, 226), (182, 77, 160), (1, 59, 132), (250, 161, 9), (248, 187, 112), (128, 65, 16), (30, 41, 48), (116, 91, 34), (198, 151, 47), (112, 113, 94), (0, 119, 100), (186, 72, 20), (250, 219, 66), (177, 124, 90), (109, 102, 144), (232, 220, 182), (255, 235, 26), (61, 74, 82), (209, 56, 138)]

def line_dot():
    for i in range(1, 10):
        turtle.pendown()
        turtle.dot(20, random.choice(colour_list))
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
turtle.penup()

turtle.setx(-200)
turtle.sety(-200)

for i in range(10):
    line_dot()
    turtle.dot(20, random.choice(colour_list))
    if i%2 == 0:
        turtle.setheading(90)
        turtle.penup()
        turtle.forward(50)
        turtle.setheading(180)
    elif i == 9:
        break
    else:
        turtle.setheading(90)
        turtle.penup()
        turtle.forward(50)
        turtle.setheading(0)


turtle.exitonclick()

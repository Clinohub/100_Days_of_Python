# Racing with Turtle Graphics 
# 100 Days of Code ! Day 19


import turtle
import random

#turtle screen dimension
turtle.setup(width = 500, height = 400)
user_bet = turtle.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")

turtle.speed("fastest")
turtle.hideturtle()
#Starting Line
turtle.penup()
turtle.goto(x=-210, y=150)
turtle.right(90)
turtle.pendown()
turtle.forward(300)

#Finishing Line
turtle.penup()
turtle.goto(x=230, y=150)
turtle.setheading(0)
turtle.right(90)
turtle.pendown()
turtle.forward(300)

colours = ["red","orange","yellow","green","blue","purple"]

#turtle Instances
redT=turtle.Turtle(shape = "turtle")
redT.color(colours[0])
redT.penup()
redT.goto(x=-230,y=50)

orangeT=turtle.Turtle(shape = "turtle")
orangeT.color(colours[1])
orangeT.penup()
orangeT.goto(x=-230,y=-50)

yellowT=turtle.Turtle(shape = "turtle")
yellowT.color(colours[2])
yellowT.penup()
yellowT.goto(x=-230,y=100)

greenT=turtle.Turtle(shape = "turtle")
greenT.color(colours[3])
greenT.penup()
greenT.goto(x=-230,y=-100)

blueT=turtle.Turtle(shape = "turtle")
blueT.color(colours[4])
blueT.penup()
blueT.goto(x=-230,y=150)

purpleT=turtle.Turtle(shape = "turtle")
purpleT.color(colours[5])
purpleT.penup()
purpleT.goto(x=-230,y=0)

participants = [redT,orangeT,yellowT,greenT,blueT,purpleT]
turtle.speed("fast")

#turtles racing
participating = True
while participating:
    for participant in participants:
        if participant.xcor() >= 220:
            winner = participant.color()
            participating = False
        else:
            participant.fd(random.randint(1, 10))

#Winner Declaration
print(f"The winner is: {winner[0]}")
if user_bet == winner:
    print("You've won your Bet")
else:
    print("Sorry!! You've lost your Bet")

turtle.exitonclick()

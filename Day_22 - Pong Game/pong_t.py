from turtle import Turtle, Screen

right_paddle = Turtle()
screen = Screen()

screen.setup(width=800, height=600, startx=None, starty=None)
screen.bgcolor("black")
screen.title("Pong: The famous Arcade game")

right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid = 5.0, stretch_len = 1.0, outline = None) # default turtle size is 20px 
right_paddle.penup()
right_paddle.speed("fastest")
right_paddle.setx(350)

def move_up():
    up = right_paddle.ycor()
    if up <= 250:
        up += 20
        right_paddle.sety(up)

def move_down():
    down = right_paddle.ycor()
    if down >= -250:
        down -= 20
        right_paddle.sety(down)

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")



screen.exitonclick()


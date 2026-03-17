from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Creates snake body
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Appends snake body
        """
        new_segment = Turtle("square")
        new_segment.color("blue")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """
        Increases the tail of the snake
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Moves the snake body
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[seg_num - 1].xcor()
            newY = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(newX, newY)

        self.head.fd(MOVE_DISTANCE)

    def up(self):
        """
        Turns the snake head to face up
        if not facing down
        """
        if not self.head.heading() == DOWN:
            self.head.seth(UP)

    def down(self):
        """
        Turns the snake head to face down
        if not facing up
        """
        if not self.head.heading() == UP:
            self.head.seth(DOWN)

    def left(self):
        """
        Turns the snake head to face left
        if not facing right
        """
        if not self.head.heading() == RIGHT:
            self.head.seth(LEFT)

    def right(self):
        """
        Turns the snake head to face right
        if not facing left
        """
        if not self.head.heading() == LEFT:
            self.head.seth(RIGHT)


import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:

    def __init__(self):
        self.traffic = []
        self.generate_car = True
        self.cars()
        self.move_speed = STARTING_MOVE_DISTANCE
        self.move_cars()


    def cars(self):
        """
        creates a car and add to traffic
        """

        car = Turtle("square")
        car.turtlesize(stretch_wid=1.0, stretch_len=2.0)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(280, random.randrange(-240, 241, 30))
        self.traffic.append(car)


    def move_cars(self):
        for vehicle in self.traffic:
            vehicle.bk(self.move_speed)


    def speed_up(self):
        self.move_speed += MOVE_INCREMENT


    def car_distant(self):
        """
        avoids overlapping cars
        """
        if self.traffic[-1].xcor() >= 230:
            return False

        return True


    def car_is_past_screen_reset(self):
        for moving_car in self.traffic:
            if moving_car.xcor() <= -290:
                moving_car.setx(280)
                self.generate_car = False
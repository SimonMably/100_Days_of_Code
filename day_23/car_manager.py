from turtle import Turtle
import random

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_HEADING = 180
# important: think of other/better names of next 2 variables
CAR_PROBABILITY = 10
CAR_PROBABILITY_THRESHOLD = 2
# important: coordinates = (x, y)
# notice: stay between -280 and 280 on the y-axis
# Y_POSITIONS not used
Y_POSITIONS = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200, -250]


class CarManager:
    """Randomly generates car objects to the screen. Controls behaviour and
    appearance of car objects."""
    # todo: cars randomly generate along y-axis DONE
    # todo: to have multiple cars on screen at once, append cars to a list DONE
    # todo: cars will move from right edge of screen to the left edge DONE
    # todo: at games start, all cars move at 'STARTING_MOVE_DISTANCE' speed DONE
    # todo: at each new level, use 'MOVE_INCREMENT' to increase car speed REWORK

    def __init__(self):
        # super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.probability_threshold = CAR_PROBABILITY_THRESHOLD
        self.generate_starting_cars()
        self.generate_starting_positions()

    def create_car(self):
        """Creates car objects with random colours."""
        car = Turtle(shape="square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLOURS))
        car.setheading(CAR_HEADING)
        car.penup()
        # random_y = random.randint(-250, 250)
        # car.goto()
        self.cars.append(car)

    def generate_new_car(self):
        """Adds new car to self.cars list."""
        amount = random.randint(0, CAR_PROBABILITY)
        if amount < self.probability_threshold:
            self.create_car()
            self.cars[-1].goto(300, random.randrange(-240, 240))

    def generate_starting_cars(self):
        """Generates cars at beginning of game."""
        # important: may change numbers in random.randint()
        starting_cars_amount = random.randint(15, 30)
        for car in range(starting_cars_amount):
            self.create_car()
        print(f"Generated {len(self.cars)} starting cars.")

    def generate_starting_positions(self):
        """Generates a starting position for each car in self.cars"""
        for car in self.cars:
            car.goto(random.randint(-250, 250), random.randrange(-240, 240))

    def regenerate_cars(self):
        """When each car reaches left edge of the screen, they regenerate in
        a random location along the same line."""
        # FIX: maybe reword docstring
        for car in self.cars:
            if car.xcor() < -300:
                random_y = random.randint(-250, 250)
                car.goto(300, random_y)

    def move_cars(self):
        """Moves cars from left edge of screen to right side of screen."""
        for car in self.cars:
            car.forward(self.car_speed)

    def increase_car_speed(self):
        """If player reaches a new level, increase speed of cars in self.cars"""
        self.car_speed += MOVE_INCREMENT

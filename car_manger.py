from turtle import Turtle
import random

START_MOVE_DISTANCE = 5  # Starting speed of the cars
MOVE_INCREMENT = 10  # Increment in speed as the game progresses


def colors_rgb():
    colors = []
    for color in range(3):
        r_color = random.randint(0, 255)  # Generate a random color value between 0 and 255
        colors.append(r_color)
    return tuple(colors)  # Return the random RGB color as a tuple


class CarManager:
    def __init__(self):
        super().__init__()  # Initialize the parent class (not needed here, but included)
        self.all_cars = []  # List to store all cars
        self.car_speed = START_MOVE_DISTANCE  # Set initial speed for cars

    def create_car(self):
        # Chance of creating a new car each time this function is called
        random_chance = random.randint(1, 3)  # Randomly decide whether to create a car
        if random_chance == 1:  # 1 out of 3 chance to create a car
            new_car = Turtle("square")  # Create a new square car
            new_car.penup()  # Lift the pen to avoid drawing lines
            new_car.color(colors_rgb())  # Set the car's color to a random RGB value
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Resize the car to look like a rectangle
            new_car.goto(300, random.randint(-250, 250))  # Position the car at the right side of the screen
            self.all_cars.append(new_car)  # Add the new car to the list

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move each car backward by the current speed

    def level_up(self):
        self.car_speed += MOVE_INCREMENT  # Increase the car speed as the game level increases

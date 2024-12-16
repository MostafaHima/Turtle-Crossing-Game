from turtle import Turtle

STARTING_POSITION = (0, -280)  # Starting position of the player
MOVE_DISTANCE = 10  # Distance the player moves per step
FINSH_LINE_Y = 280  # Y-coordinate for the finish line


class Player(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent class (Turtle)
        self.setheading(90)  # Set the heading of the turtle to face upward
        self.turtlesize(stretch_wid=1.5)  # Resize the turtle for better visibility
        self.color("black")  # Set the color of the turtle to black
        self.shape("turtle")  # Set the shape of the turtle to "turtle"
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(STARTING_POSITION)  # Move the turtle to the starting position
        self.finsh_line()  # Set the initial finish line position


    def move_up(self):
        self.forward(MOVE_DISTANCE)  # Move the player upward by the specified distance

    def finsh_line(self):
        self.seth(90)  # Set heading to face upwards
        self.goto(STARTING_POSITION)  # Reset the player to the starting position

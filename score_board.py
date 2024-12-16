from turtle import Turtle

FONT = ("Arial", 20, "normal")  # Define the font for displaying text

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent class (Turtle)
        self.score = 0  # Initialize score to 0
        self.hideturtle()  # Hide the turtle to only display text
        self.penup()  # Lift the pen to avoid drawing lines
        self.update_level()  # Update the level display at the start

    def update_level(self):
        self.goto(-270, 250)  # Move to the position where the score is displayed
        self.pendown()  # Start drawing
        self.write(f"Level {self.score}", font=FONT)  # Display the current level (score)

    def add_score(self):
        self.clear()  # Clear the previous score display
        self.score += 1  # Increase the score by 1
        self.update_level()  # Update the score display with the new level

    def end_game(self):
        self.goto(-70, 0)  # Move to the center of the screen
        self.write("Game Over", font=("Arial", 20, "bold"))  # Display the "Game Over" message

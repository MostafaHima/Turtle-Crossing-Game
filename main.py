def play():
    import time
    import turtle
    from turtle import Screen
    from player import Player
    from car_manger import CarManager
    from score_board import ScoreBoard

    turtle.colormode(255)  # Set the color mode to RGB (0-255)
    screen = Screen()  # Create a screen object
    screen.setup(height=600, width=600)  # Set up screen size
    screen.bgcolor("floral white")  # Set background color
    turtle.tracer(0)  # Disable automatic screen updates to control when to update it

    player = Player()  # Create a player object
    score_board = ScoreBoard()  # Create a score board object

    # Bind the 'Up' arrow key to the player's move_up method
    screen.onkeypress(fun=player.move_up, key="Up")
    screen.listen()  # Start listening for keypresses
    car_manger = CarManager()  # Create a car manager object

    is_on_game = True  # Initialize the game status as True
    while is_on_game:
        time.sleep(0.1)  # Pause the game for a short time to control speed
        screen.update()  # Update the screen manually

        # Check if the player has crossed the finish line
        if player.ycor() > 280:
            player.finsh_line()  # Reset the player's position
            car_manger.level_up()  # Increase the car speed
            score_board.add_score()  # Update the score

        car_manger.create_car()  # Create new cars
        car_manger.move()  # Move the cars

        # Check for collisions between the player and the cars
        for car in car_manger.all_cars:
            if player.distance(car) < 25:  # If the player is close enough to a car
                is_on_game = False  # End the game
                score_board.end_game()  # Display "Game Over" message

    screen.mainloop()  # Keep the screen open after the game ends

play()  # Call the play function to start the game



























































# Jackson Hauley - Fix the game raid

# Importing
import random

# Defining Functions
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 1 # This bug would make it so it takes 11 guesses because it marks your first guess as guess 0, this was a ligic aerror, it gave you 11 guesses instead of 10
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: ")) # There was a string input when it wanted an int, this is syntax bug, it made the game crash 
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            print("Game Over. Thanks for playing!") # The problem is that the game over thing is in the wrong spot because it runs even when you win which is bad apparently, this is a logic error, and it makes the game run game over when you win AND lose which was bad apparently
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts += 1 # There was no adding attempts by 1 so it never reached max attemps, this is a logic error, it made the game not print your max attempts if you have used all of them
        elif guess < number_to_guess:
            print("Too low! Try again.") 
            attempts += 1 # Add the attempts here also
        continue
    

# Startup
start_game()
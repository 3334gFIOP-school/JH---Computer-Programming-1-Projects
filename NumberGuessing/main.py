# Jackson Hauley - Number Guessing RAID

# Declaration
import random
number = random.randint(1,100)
tries = 0

# UI
print("\nRandom Number Guesser\n==================================")

# Calculations
def start():
    global tries
    guess = int(input("Pick a number from 1 to 100: "))
    if guess == number:
        print("You guessed it!")
        print(f"The number was {number}!")
        print(f"It took you {tries} tries!")
    elif guess < number:
        tries += 1
        print("You guessed too low!")
        start()
    elif guess > number:
        tries += 1
        print("You guessed too high!")
        start()

# Running
start()
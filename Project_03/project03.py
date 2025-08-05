"""
The perfect guess

We are going to write a program that generates a random number and ask the user to guess it.
If the players guess is higher than the actual number, the program displays 'Lower number please'. Similarly
if the user's guess it too low, the program prints 'Higher number please' when the user's guesses the correct
number, the program displays the number of guesses the player used to arrive at the number.

hint: use the random module
"""

""" 
import random

actual_number = random.randint(1,10)

guess = int(input("Guess a number 1 to 10: "))

print("The actual number is: ",  actual_number)

if (actual_number < guess):
    print("Lower Number Please")

elif (actual_number > guess):
    print("Higher Number Please...")

elif (actual_number == guess):
    print("You are right.. Well Done!")

"""

# Improvement Code

import random

# Initialize the guess count
guess_count = 0

# Run a loop until the correct number is guessed
while True:
    # Generate the random number
    actual_number = random.randint(1, 10)

    guess = int(input("Guess a number between 1 to 10: "))
    guess_count += 1

    print(f"[Attempt {guess_count}] The actual number is: {actual_number}")

    if guess > actual_number:
        print("Lower number please.")
    elif guess < actual_number:
        print("Higher number please...")
    else:
        print(f"You are right.. Well Done!")
        print(f"You guessed the number in {guess_count} attempts.")
        break

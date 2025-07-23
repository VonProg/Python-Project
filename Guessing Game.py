# Number Guessing Game

import random

guessing_number = random.randint(1, 10)
attempts = 0

print("Guess the number between 1 and 10!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < guessing_number:
        print("Too low! Try again.")
    elif guess > guessing_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} attempts.")
        break

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
print("Choose a difficulty. Type 'easy' or 'hard': ")
difficulty = input()


def guess_number():
    user_guess = int(input("Make a guess: "))
    if user_guess == number:
        return 1
    elif user_guess < number:
        return 2
    else:
        return 3


if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")

stop = 0
while attempts > 0 and stop == 0:
    result = guess_number()
    if result == 1:
        print("You win. Game over!")
        stop = 1

    elif result == 2:
        print("Too low")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        print("Too high")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
    print("Guess again")
if attempts == 0:
    print(f"The number was: {number}")
    print("You lose. Game over!")

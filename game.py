"""A number-guessing game."""

import random

print("Hello! Welcome to the number guessing game!")

name = input("What is your name? ")

print(f"Welcome, {name}. This program generates a random number between 1-100. Please try to guess what that number is.")

random_number = random.randrange(1,100)
guess = None
number_guesses = 0


while random_number != guess:

    try:
        guess = int(input("Your guess? "))
    except:
        print("You didn't input a number!! How dare you!!")
        continue

    if guess < 1 or guess > 101:
        print("How dare you!! Please enter a number between 1-100.") 
    elif guess != random_number:
        if guess > random_number:
            print("Too high! Please try again.")
            number_guesses += 1
        elif guess < random_number:
            print("Too low! Please try again.")
            number_guesses += 1

print(f"Congratulations! You got the correct number! You found the number in {number_guesses} many tries.")


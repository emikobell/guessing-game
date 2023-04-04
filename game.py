"""A number-guessing game."""

import random

print("Hello! Welcome to the number guessing game!")

name = input("What is your name? ")

print(f"Welcome, {name}. This program generates a random number between 1-100. Please try to guess what that number is.")

def play_game():

    continue_playing = True
    score = None

    while continue_playing:

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

        if score == None or score > number_guesses:
            score = number_guesses
             


        print(f"Congratulations! You got the correct number! You found the number in {number_guesses} many tries.")
        print(f"Your best score is {score}")

        play_again = input("Would you like to play again? Type y for yes, and n for no. ")

        if play_again == "y":
            continue
        elif play_again == "n":
            continue_playing = False
        else:
            print("Invalid answer. Game will stop.")
            continue_playing = False

play_game()


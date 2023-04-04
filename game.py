def play_game():
    
    """A number-guessing game."""

    import random
    
    print("Hello! Welcome to the number guessing game!")

    name = input("What is your name? ")

    custom_range = input(f"Welcome, {name}. This program generates a random number between 1-100 or you can choose a custom range. " +
                          "Would you like to use a custom range? Answer y for yes or n for no. ")
    
    lower_range = 1
    higher_range = 100
    
    if custom_range == "y":
        print("Please tell us the lower range: ")
        lower_range = int(input("> "))
        print("Please tell us the higher range: ")
        higher_range = int(input("> "))
    elif custom_range == "n":
        pass
    else:
        print("Invalid input. The game will use the standard range between 1-100.")

    continue_playing = True
    score = None

    while continue_playing:

        print("Ready? Please try to guess what the number is.")

        random_number = random.randrange(lower_range, higher_range)
        guess = None
        number_guesses = 0

        while random_number != guess:

            try:
                guess = int(input("Your guess? "))
            except:
                print("You didn't input a number!! How dare you!!")
                continue

            if guess < lower_range or guess > higher_range:
                print("How dare you!! Please enter a number within the range.") 
            elif guess != random_number:
                if guess > random_number:
                    print("Too high! Please try again.")
                    number_guesses += 1
                elif guess < random_number:
                    print("Too low! Please try again.")
                    number_guesses += 1

            if number_guesses > 10:
                print("TOO MANY TRIES!!")
                break
        
        if random_number == guess:
            number_guesses += 1
            # Captures correct guess as a guess
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

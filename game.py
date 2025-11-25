import random

# Game Introduction
print("Welcome to the Game!")
print("The goal of the game is to guess the number I'm thinking of between 1 and 100.")

# Difficulty Selection
difficulty_level = input("Choose a difficulty level (easy, medium, hard): ")
if difficulty_level == "easy":
    attempts = 10
elif difficulty_level == "medium":
    attempts = 5
elif difficulty_level == "hard":
    attempts = 3
else:
    print("Invalid difficulty level. Defaulting to medium.")
    attempts = 5

# Game Start After Difficulty Selection
print("")
print("You have selected", difficulty_level, "difficulty.\nYou have", attempts, "attempts to guess the number.")

# Random Number Generation
number_to_be_guessed = int(random.randint(1,100))

# User Guessing Loop
print("")
guess = int(input("Make your first guess: "))

while guess != number_to_be_guessed and attempts > 1:
    attempts -= 1
    if guess < number_to_be_guessed:
        print("Too low!")
    elif guess > number_to_be_guessed:
        print("Too high!")
    
    print("You have", attempts, "attempts remaining.")
    guess = int(input("Make another guess: "))

# End of the Game
if guess == number_to_be_guessed:
    print("Congratulations! You've guessed the number:", number_to_be_guessed)
else:
    print("Sorry, you've run out of attempts. The number was:", number_to_be_guessed)


import random

print("Welcome to the Game!")
print("The goal of the game is to guess the number I'm thinking of between 1 and 100.")

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

print("")
print("You have selected", difficulty_level, "difficulty.\nYou have", attempts, "attempts to guess the number.")

number_to_be_guessed = int(random.randint(1,100))

print("")
guess = int(input("Make your first guess: "))

while guess != number_to_be_guessed and attempts > 1:
    attempts -= 1
    if guess < number_to_be_guessed:
        print("Too low!")
    elif guess > number_to_be_guessed:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number!")



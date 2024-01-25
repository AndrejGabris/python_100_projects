# TODO1 libraries replit/random
import random
from replit import clear
from art import logo

# TODO2 opening text: Welcome to the Number Guessing Game! I'm  thinking of a number between 1 and 100. Choose a difficulty. Type 'easy' = 10 attempts to guess or 'hard' = 5 attempts to guess:
clear()
print(logo,"")
print("Welcome to the Number Guessing Game!\nI'm  thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' = 10 attempts to guess or 'hard' = 5 attempts to guess: ")
while level != "easy" and level != "hard":
    level = input("Ooops. Wrong input. Type 'easy' = 10 attempts to guess or 'hard' = 5 attempts to guess: ")
if level == "easy":
    attempts = 10
else:
    attempts = 5

# TODO3 pick a random choice from interval
guessed_number = random.choice(range(1,101))

# TODO4 user's guess: Make a guess
user_guess = int(input("Make a guess: "))

# TODO5 compare guess and guessed number +  you won or Too high/low + attempts remaining
result = True
while result == True:
    print("")
    if attempts > 1:
        if guessed_number == user_guess:
            print(f"You got it! The answer was {guessed_number}.")
            result = False
        elif guessed_number > user_guess:
            attempts -= 1
            print("Too low.\nGuess again.")
            print(f"You have {attempts} attempts remaining to guess the number")
            user_guess = int(input("Make a guess: "))
        elif guessed_number < user_guess:
            attempts -= 1
            print("Too high.\nGuess again.")
            print(f"You have {attempts} attempts remaining to guess the number")
            user_guess = int(input("Make a guess: "))
    else:
        print(f"You lost. No more attempts remaining. The guessed number was {guessed_number}.\n")
        result = False





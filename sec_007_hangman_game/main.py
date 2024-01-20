#Step 1 
from hangman_arts import logo, stages
from hangman_words import word_list


# word_list = ["aardvark", "baboon", "camel"]
print(logo)

import random
chosen_word = random.choice(word_list)

word_length = len(chosen_word)
display = []
for letter in range(word_length):
    display.append("_")

#Testing code
print(f'Pssst, the solution is {chosen_word}.')   

end_of_the_game = True
lives = len(stages)
wrong_guesses=[]
while end_of_the_game:
    guess = input("Guess letter: ").lower()
    
    while len(guess) != 1:
        guess = input("Wrong input format, try again. Guess letter: ").lower()
    
    if guess in display:
        print(f"You have already guessed this letter: {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    print(f"{' '.join(display)}")
    print("\n")

    if guess not in chosen_word:
        print(f"Letter {guess} is not in guessed word. Remaining lives: {lives - 1}")
        if guess not in wrong_guesses:
            wrong_guesses.append(guess)
        print("You have already tried: ", f"{', '.join(wrong_guesses)}")
        print(stages[lives - 1])
        lives -= 1
        if lives == 0:
            end_of_the_game = False
            print("You lost.")
            print(f"Guessed word was: {chosen_word}")


    if "_" not in display:
        end_of_the_game = False
        print("You won.")
from hangman_list import list_of_words
from hangman_art import logo
from hangman_art import stages
import random

print(logo)

chosen_word = random.choice(list_of_words)


display = []
for index in range(len(chosen_word)):
        display += '_'

# print(chosen_word)
lives = 6
game_on = True

print("Word is "+" ".join(display)+ " long")

while game_on == True:
    guess = input("Guess a letter: ")

    if guess not in chosen_word:
            lives -= 1
            print(stages[lives])
            if lives == 0:
                game_on = False
                print(f"YOU LOST\nCORRECT WORD IS {chosen_word}") 

    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if guess == letter:
            display[index] = guess
    
    print(" ".join(display))

    if '_' not in display:
        game_on = False





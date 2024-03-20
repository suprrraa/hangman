# BANNER and HANGMAN_PICS are some ASCII art
# Create your own ASCII art if you desire, but
# ONLY AFTER getting the game logic working.
from ascii_art import BANNER, HANGMAN_PICS
from random import choice
from word_lists import animal_words

"""
Here's where you'll write your code. 
  - Follow the instructions in the README file.
  - If you try to write all the code in `play_hangman`, 
    it's going to be a mess. Instead, break your logic
    into smaller functions that you can call from 
    `play_hangman`.

Run your code from the terminal:
  - make sure you're in the right directory (`projects/hangman`)
    - if you're not sure how to get to the right directory, ask!
  - make sure you're at the command line prompt, not in the Python shell (not >>>)
  - type the following command: python hangman.py

Tests? No tests for this project. 
"""


# Here's where you can define helper functions


# `play_hangman` is the main function, the function
# that will orchestrate all the helper functions
# you define, above.
def play_hangman():

    print("Welcome To Hangman")
    x=input("press enter to start")
    secret_word = choice(animal_words)
    #print(secret_word)(use at end of game)
    guessed_word = ['_'] * len(secret_word)
    while '_' in guessed_word:
        print(' '.join(guessed_word))
        guess = input("guess a letter: ")
        # print("you guessed: ", guess)
        for index, letter in enumerate(secret_word):
            if guess == letter:
                guessed_word[index] = guess 
                if guess = 7 

        print(guessed_word)
      

      

def secret_word():
    pass

""" 
Don't worry about the code below, and don't change it.

It's just a way to trigger the `play_hangman` function
when you run this file from the command line.
"""
if __name__ == "__main__":
    play_hangman()

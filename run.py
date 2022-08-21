import random
from words import word_list

def guess_word():
    final_word = random.choice(word_list)
    return word.upper()

def lets_play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("\n Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
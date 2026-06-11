from src.pictures import *
import random

# печать виселицы
def print_hangman(errors):
    if errors == 0:
        print(error_0)
    elif errors == 1:
        print(error_1)
    elif errors == 2:
        print(error_2)
    elif errors == 3:
        print(error_3)
    elif errors == 4:
        print(error_4)
    elif errors == 5:
        print(error_5)
    elif errors == 6:
        print(error_6)
    else:
        print("Error! Picture not found!")

# печать слова с отгаданными и закрытыми буквами
def print_secret_word(word, guessed_letters):

    for num in range(len(word)):

        if num in guessed_letters:
            print(word[num], end=' ')

        else:
            print('_', end=' ')

    print('\n')

def player_win(word, guessed_letters):
    for index in range(len(word)):
        if index not in guessed_letters:
            return False
    return True

def get_secret_word():
    with open('src/words.txt', 'r') as file:
        words = file.read().splitlines()
    return random.choice(words)

def create_game():
    word = get_secret_word()
    guessed_letters = []
    errors = 0
    game_is_over = False
    return word, guessed_letters, errors, game_is_over


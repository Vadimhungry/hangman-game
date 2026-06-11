from src.pictures import images
import random

# печать виселицы
def print_hangman(errors):
    print(images[errors])

# печать слова с отгаданными и закрытыми буквами
def print_secret_word(word, guessed_letters):

    for letter in word:

        if letter in guessed_letters:
            print(letter, end=' ')

        else:
            print('_', end=' ')

    print('\n')

def player_win(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def get_secret_word():
    with open('src/words.txt', 'r') as file:
        words = file.read().splitlines()
    return random.choice(words)

def create_game():
    word = get_secret_word()
    guessed_letters = set()
    errors = 0
    return word, guessed_letters, errors

def ask_for_continue():
    replay = input('Начать игру заново? (да/нет) ')

    if replay == 'да':
        return create_game()

    else:
        print('Игра завершена!')
        exit()


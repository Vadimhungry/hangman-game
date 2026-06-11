import random
import utils

words = ['цветок']

while True:
    word = random.choice(words)

    guessed_letters = []
    errors = 0

    while True:

        utils.print_hangman(errors)
        utils.print_secret_word(word, guessed_letters)

        guess = input('Угадай букву: ')

        if guess in word:

            for num, letter in enumerate(word):
                if letter == guess:
                    guessed_letters.append(num)

        else:
            errors += 1

        if errors == 6:
            print('Ты проиграл!')
            break

        if len(guessed_letters) == len(word):
            print('Победа! Слово угадано!')
            utils.print_secret_word(word, guessed_letters)
            break

    replay = input('Начать игру заново? (да/нет) ')

    if replay == 'да':
        continue
    else:
        print('Игра завершена!')
        exit()
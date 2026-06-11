import random

words = ['цветок']

while True:
    word = random.choice(words)

    guessed_letters = []
    errors = 0

    while True:

        # рааспечатываем слово с отгаданными буквами
        for num in range(len(word)):

            if num in guessed_letters:
                print(word[num], end=' ')

            else:
                print('_', end=' ')
        print('\n')

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

            # рааспечатываем слово с отгаданными буквами
            for num in range(len(word)):

                if num in guessed_letters:
                    print(word[num], end=' ')

                else:
                    print('_', end=' ')
            print('\n')
            break

    replay = input('Начать игру заново? (да/нет) ')

    if replay == 'да':
        continue
    else:
        print('Игра завершена!')
        exit()
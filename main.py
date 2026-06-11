from src import utils


word, guessed_letters, errors, game_is_over = utils.create_game()

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
        game_is_over = True

    # todo переписать на множества
    if utils.player_win(word, guessed_letters):
        print('Победа! Слово угадано!')
        utils.print_secret_word(word, guessed_letters)
        game_is_over = True

    if game_is_over:
        replay = input('Начать игру заново? (да/нет) ')

        if replay == 'да':
            word, guessed_letters, errors, game_is_over = utils.create_game()
            continue
        else:
            print('Игра завершена!')
            exit()
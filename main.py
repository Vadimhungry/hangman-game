from src import utils


word, guessed_letters, errors = utils.create_game()

while True:

    utils.print_hangman(errors)
    utils.print_secret_word(word, guessed_letters)

    guess = input('Угадай букву: ')

    if guess in word:
        guessed_letters.add(guess)

    else:
        errors += 1

    if errors == 6:
        print('Ты проиграл!')

    elif utils.player_win(word, guessed_letters):
        print('Победа! Слово угадано!')

    if errors == 6 or utils.player_win(word, guessed_letters):
        word, guessed_letters, errors = utils.ask_for_continue()

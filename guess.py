import sys
from game import *
from stringDatabase import *


def check_guess_if_letter_enter(letter, word):
    """
    Checks whether the letter is in the word or not.
    :param letter: character
    :param word: string : An actual guess word hidden from the user
    :return: boolean. True if that letter is in the guess word otherwise false
    """
    if letter in word:
        for single_cha in range(0, len(word)):
            if letter == word[single_cha]:
                return True
    return False


def update_screen_output(letter, word, output):
    """
    This function basically fill in the blanks for the guess word
    which is being shown to the player.
    :param letter:  character to be filled in the places of hyphen
    :param word:  string : word
    :param output: string : current output string which is displayed to the user
    :return: output string with letter filled in it's respective position in the word
    """
    found_letter = 0
    for i in range(0, len(word)):
        if letter == word[i]:
            found_letter += 1
            output = output[:i] + letter + output[i + 1:]
    print(f'************************************')
    print(f' You found {found_letter} letter(s)')
    print(f'************************************')
    return output


def display_score(games):
    """
    Creates a table structure for displaying the scoreboard to the player.
    :param games: List of all games played; as list of game class objects
    """
    game_string = "Game"
    word_string = "Word"
    status_string = "Status"
    bad_string = "Bad Guesses"
    missed_string = "Missed Letters"
    score_string = "Score"
    hyphens_string = "---------"
    final_score = 0

    print(f'{game_string.ljust(20)}{word_string.ljust(20)}'
          f'{status_string.ljust(20)}{bad_string.ljust(20)}'
          f'{missed_string.ljust(20)}{score_string.ljust(20)}')

    print(f'{hyphens_string.ljust(20)}{hyphens_string.ljust(20)}'
          f'{hyphens_string.ljust(20)}{hyphens_string.ljust(20)}'
          f'{hyphens_string.ljust(20)}{hyphens_string.ljust(20)}')

    for (index, game) in enumerate(games):
        status_string = "Success" if game.status else "Gave up"
        final_score += game.score
        print(f'{str(index + 1).ljust(20)}{str(game.actual_word).ljust(20)}'
              f'{str(status_string).ljust(20)}{str(game.bad_guesses).ljust(20)}'
              f'{str(game.missed_letters).ljust(20)}{str(round(game.score, 2)).ljust(20)}')
    print(f'Final Score : {final_score:.2f}')
    pass


def get_blank_spaces(player_word):
    """
    Get the index of the blank spaces at a particular time
    :param player_word: the current state of the output screen word which player has guessed already
    :return: the list of index position where - is found
    """
    blanks_index = []
    for i in range(len(player_word)):
        if player_word[i] == "-":
            blanks_index.append(i)
    return blanks_index


def get_frequency_for_character(alphabet):
    """
    This function maps the frequency of the alphabet from the game.py file
    characters range from lowercase a to lowercase z
    :param alphabet: character for which the frequency is wanted
    :return: number
    """
    return letter_frequencies.get(alphabet, None)


def get_total_frequency_for_blank(actual_word, blank_spaces):
    """
    Counts the total frequency of the letter which was at the blank space by
    mapping the respective frequency together and summing it up
    :param actual_word:
    :param blank_spaces:
    :return: total frequency
    """
    total = 0
    for space in blank_spaces:
        try:
            total += get_frequency_for_character(actual_word[space])
        except:
            print(f'No frequency associated with letter {actual_word[space]}')
    return total


def get_maximum_score_for_word(actual_word):
    """
    Calculates the maximum score for the current guessed word
    :param actual_word:
    :return:
    """
    total = 0
    for i in range(len(actual_word)):
        total += get_frequency_for_character(actual_word[i])
    return total


def calculate_score(games):
    """
    This function is only responsible for calculating the score for each game.
    It will calculate the score and will update the score variable for each objects
    :param games: List of game class object
    """
    for (index, game) in enumerate(games):
        blank_spaces = get_blank_spaces(game.player_word)
        total_frequency_count = get_total_frequency_for_blank(game.actual_word, blank_spaces)
        if game.status:
            game.score = total_frequency_count / game.letters_tried if game.letters_tried > 0 else total_frequency_count
            if game.bad_guesses > 0:
                for i in range(game.bad_guesses):
                    game.score -= game.score * 0.10

        if not game.status:
            game.score = 0 - total_frequency_count
    pass


def start_game():
    """
    This is the main function which is responsible for starting the game after loading the
    data dictionary file which contains the words which are to be guessed.
    """
    file_name = 'four_letters.txt'
    games = []
    try:
        guess_word = get_random_word(file_name)
        new_game = Game(guess_word)
        games.append(new_game)
    except IOError:
        print(f'Oops ! The file {file_name} mentioned in the code do not exist !')
        sys.exit(1)

    playing = True
    screen_output = "-" * len(guess_word)
    new_game.player_word = screen_output
    print(f'*****************************')
    print(f'** The great guessing game **')
    print(f'*****************************')
    while playing:
        print(f'Current guess {screen_output}')
        option = input('g = guess, t = tell, l = letter, q = quit\n')
        if option.lower() == 'g':
            whole_word_guess = input('Enter the whole word!\n').lower()
            if whole_word_guess == guess_word:
                print(f'Congratulations ! You guess the word')
                new_game.status = True
                new_game.player_word = screen_output
                guess_word = get_random_word(file_name)
                print(f'*****************************')
                print(f'** The great guessing game **')
                print(f'*****************************')
                new_game = Game(guess_word)
                games.append(new_game)
                screen_output = "-" * len(guess_word)
            else:
                print(r'OOPS ! You guessed it wrong. Please try again.')
                new_game.bad_guesses = new_game.bad_guesses + 1
        elif option.lower() == 't':

            print(f'*****************************')
            print(f'The word was {guess_word} ')
            print(f'*****************************')

            print(f'Let\'s see if you can guess the next one.')
            guess_word = get_random_word(file_name)
            print(f'*****************************')
            print(f'** The great guessing game **')
            print(f'*****************************')
            new_game.player_word = screen_output
            new_game = Game(guess_word)
            games.append(new_game)
            screen_output = "-" * len(guess_word)
        elif option.lower() == 'l':
            input_letter = input('Enter the letter:\n')[0].lower()
            new_game.letters_tried += 1
            if check_guess_if_letter_enter(input_letter, guess_word):
                screen_output = update_screen_output(input_letter, guess_word, screen_output)
                new_game.player_word = screen_output
            else:
                new_game.missed_letters = new_game.missed_letters + 1
            if "-" not in screen_output:
                print('Congratulations! You guess the word\n')
                new_game.status = True
                guess_word = get_random_word(file_name)
                print(f'*****************************')
                print(f'** The great guessing game **')
                print(f'*****************************')
                new_game = Game(guess_word)
                games.append(new_game)
                screen_output = "-" * len(guess_word)
        elif option.lower() == 'q':
            playing = False
            games.pop()
            calculate_score(games)
            display_score(games)
        else:
            print('Wrong option selected ! Please try again\n')
    pass


try:
    start_game()
except KeyboardInterrupt:
    print(f'You have stopped the program !')

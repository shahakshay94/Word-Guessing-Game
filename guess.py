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
    for i in range(0, len(word)):
        if letter == word[i]:
            output = output[:i] + letter + output[i + 1:]

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

    print(f'{game_string.ljust(20)}{word_string.ljust(20)}'
          f'{status_string.ljust(20)}{bad_string.ljust(20)}'
          f'{missed_string.ljust(20)}{score_string.ljust(20)}')

    print(f'{hyphens_string.ljust(20)}{hyphens_string.ljust(20)}'
          f'{hyphens_string.ljust(20)}{hyphens_string.ljust(20)}'
          f'{hyphens_string.ljust(20)}{hyphens_string.ljust(20)}')

    for (index, game) in enumerate(games):
        print(f'{str(index + 1).ljust(20)}{str(game.actual_word).ljust(20)}'
              f'{str(game.status).ljust(20)}{str(game.bad_guesses).ljust(20)}'
              f'{str(game.missed_letters).ljust(20)}{str(game.score).ljust(20)}')


def get_blank_spaces(player_word):
    blanks_index = []
    for i in range(len(player_word)):
        if player_word[i] == "-":
            blanks_index.append(i)
    return blanks_index


def get_frequency_for_character(alphabet):
    return letter_frequencies.get(alphabet, None)


def get_total_frequency_for_blank(actual_word, blank_spaces):
    total = 0
    for space in blank_spaces:
        try:
            total += get_frequency_for_character(actual_word[space])
        except:
            print(f'No frequency associated with letter {actual_word[space]}')
            sys.exit(1)
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
        game.score = total_frequency_count
        # print(total_frequency_count)
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
    print(f'** The great guessing game ---->** {guess_word}')
    while playing:
        print(f'Current guess {screen_output}')
        option = input('g = guess, t = tell, l = letter, q = quit\n')
        if option.lower() == 'g':
            whole_word_guess = input('Enter the whole word!\n').lower()
            if whole_word_guess == guess_word:
                print(r'Congratulations ! You guess the word')
                new_game.status = True
                new_game.player_word = screen_output
                guess_word = get_random_word(file_name)
                print(f'** The great guessing game ---->** {guess_word}')
                new_game = Game(guess_word)
                games.append(new_game)
                screen_output = "-" * len(guess_word)
            else:
                print(r'OOPS ! You guessed it wrong. Please try again.')
                new_game.bad_guesses = new_game.bad_guesses + 1
        elif option.lower() == 't':
            print(f'The word was {guess_word}')
            print(f'Let\'s see if you can guess the next one.')
            guess_word = get_random_word(file_name)
            print(f'** The great guessing game ---->** {guess_word}')
            new_game.player_word = screen_output
            new_game = Game(guess_word)
            games.append(new_game)
            screen_output = "-" * len(guess_word)
        elif option.lower() == 'l':
            input_letter = input('Enter the letter:\n')[0].lower()
            if check_guess_if_letter_enter(input_letter, guess_word):
                screen_output = update_screen_output(input_letter, guess_word, screen_output)
                new_game.player_word = screen_output
            else:
                new_game.missed_letters = new_game.missed_letters + 1
            if "-" not in screen_output:
                print('Congratulations ! you guess the word\n')
                new_game.status = True
                guess_word = get_random_word(file_name)
                print(f'** The great guessing game ---->** {guess_word}')
                new_game = Game(guess_word)
                games.append(new_game)
                screen_output = "-" * len(guess_word)
        elif option.lower() == 'q':
            playing = False
            calculate_score(games)
            display_score(games)
        else:
            print('Wrong option selected ! Please try again\n')


start_game()
# for line in open('four_letters.txt'):
#     print(line, end='')

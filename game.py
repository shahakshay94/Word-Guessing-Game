class Game:
    def __init__(self, actual_word, bad_guesses=0, status=False, missed_letters=0, score=0, player_word=""):
        """
        Creates an object for each game played by the user.
        Just like constructor.
        :param score: number; Score for that game
        :param player_word: string ; At the time of quitting/tell/guess the player word
        :param actual_word: string ; word which player needs to guess
        :param bad_guesses: number ; total number of bad guesses
        :param status: boolean ; whether the player won that round
        :param missed_letters: number ; total number of miss-guessed letters
        """
        self.actual_word = actual_word
        self.bad_guesses = bad_guesses
        self.status = status
        self.missed_letters = missed_letters
        self.score = score
        self.player_word = player_word


letter_frequencies = dict({
    'a': 1,
    'b': 1,
    'c': 1,
    'd': 1,
    'e': 1,
    'f': 1,
    'g': 1,
    'h': 1,
    'i': 1,
    'j': 1,
    'k': 1,
    'l': 1,
    'm': 1,
    'n': 1,
    'o': 1,
    'p': 1,
    'q': 1,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 1,
    'w': 1,
    'x': 1,
    'y': 1,
    'z': 1
})
# letter_frequencies = dict({
#     'a': 8.17,
#     'b': 1.49,
#     'c': 2.78,
#     'd': 4.25,
#     'e': 12.07,
#     'f': 2.23,
#     'g': 2.02,
#     'h': 6.09,
#     'i': 6.97,
#     'j': 0.15,
#     'k': 0.77,
#     'l': 4.03,
#     'm': 2.41,
#     'n': 6.75,
#     'o': 7.51,
#     'p': 1.93,
#     'q': 0.10,
#     'r': 5.99,
#     's': 6.33,
#     't': 9.06,
#     'u': 2.76,
#     'v': 0.98,
#     'w': 2.36,
#     'x': 0.15,
#     'y': 1.97,
#     'z': 0.07
# })


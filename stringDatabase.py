import random


def get_random_word(file_name):
    """
    Reads a file passed as a string. User can pass the absolute path
    or can just mention the name of the path. Chooses a random word
    from the file after reading the file.
    :param file_name: string
    :return: A random word: string
    """
    random_line = random.choice(list(open(file_name)))
    return random.choice(random_line.split())

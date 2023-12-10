" Docstring goes here - CS 5001 - Day 5 - Steve Shafer"

import string


def word_cleanup(raw_word):
    """ Clean up raw string

    Args:
        raw_word (string): string to be cleaned up

    Returns:
        string: cleaned up version

    Cleanup includes:
        strip whitespace from both ends
        remove punctuation
        force to lower case
    """
    result = "".join(ch for ch in raw_word.strip()
                     if ch not in string.punctuation)
    return result.lower()


with open("../Data Files/american-english-large.txt", "r", newline="")\
        as word_list_file:
    raw_word_list = word_list_file.readlines()
word_list = [word_cleanup(word) for word in raw_word_list]

with open("../Data Files/The Raven.txt", "r", newline="") as book_file:
    raw_book_lines = book_file.readlines()
book_lines = [word_cleanup(book_line) for book_line in raw_book_lines
              if book_line.isascii()]

word_dict = dict()
for book_line in book_lines:
    word_list = book_line.split()
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

print(word_dict)

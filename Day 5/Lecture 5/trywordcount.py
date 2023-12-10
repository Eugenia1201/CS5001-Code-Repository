" "

import string

wordlist_filename =\
    "../Data Files/american-english-large.txt"
book_filename = "../Data Files/The Raven.txt"
# The Raven
# Alice In Wonderland
# Moby Dick

with open(wordlist_filename, "r", newline="") as wordlist_file:
    raw_wordlist = wordlist_file.readlines()
wordlist = [w.strip().lower() for w in raw_wordlist if w.strip().isascii()]
# print(wordlist)

word_count = dict()
for w in wordlist:
    word_count[w] = 0

with open(book_filename, "r", newline="") as book_file:
    book_strings = book_file.readlines()
for s in book_strings:
    w_list = "".join((" " if ch in string.punctuation else ch.lower())
                     for ch in s.strip()).split()
    # print(w_list)
    for w in w_list:
        if w in word_count:
            word_count[w] += 1

print([(word, word_count[word]) for word in word_count
       if (word_count[word] > 0)])

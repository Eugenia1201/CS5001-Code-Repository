""" CS 5001 - Fall 2023 - Lab 3 - Part 1 - List of Lists

by Steve Shafer
"""

import random


def pretty_print(nested_list):
    """ Pretty-print a list of lists

    Args:
        nested_list (list of lists): A nested list of lists to be
        pretty-printed
    """
    print("[")
    for inner_list in nested_list:
        print(f"    {inner_list}")
    print("]")


number_of_lists = random.randrange(6, 13)
# remember the range doesn't include the end number

list_of_lists = []
for list_number in range(number_of_lists):
    new_list = [random.randrange(0, 101) for item_number in
                range(random.randrange(4, 11))]
    list_of_lists.append(new_list)

# Step 2
pretty_print(list_of_lists)

# Step 3

# A: Longest list
list_of_lengths = [len(this_list) for this_list in list_of_lists]
print(list_of_lengths)
longest_list = list_of_lists[list_of_lengths.index(max(list_of_lengths))]
print(f"The longest list is: {longest_list}")

# B: First two put together
print(f"The first two put together makes: {list_of_lists[0]+list_of_lists[1]}")

# C: Square of the first list
list_of_squares = [(this_item*this_item) for this_item in list_of_lists[0]]
print(f"The square of the first list is: {list_of_squares}")

# D: Big numbers
big_list_of_lists = [[this_item for this_item in this_list if this_item >= 50]
                     for this_list in list_of_lists]
print("The big numbers are:")
pretty_print(big_list_of_lists)

# E: Maximum numbers
list_of_maxes = [max(this_list) for this_list in list_of_lists]
print(f"The maximum numbers are: {list_of_maxes}")

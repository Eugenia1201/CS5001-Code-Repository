"""My sort function."""

import time
import random


sort_name = "MY SORT"

PRINT_LIMIT = 150


def sort_list(list_to_sort, display_update):
    """Sort list using My Sort.

    Args:
        list_to_sort (list of numbers): The list to sort
            will not be modified during the sort
        display_update (function): Call this to update the display

    Returns:
        process time elapsed
        sorted list
    """
    the_list = list_to_sort.copy()

    start_time = time.process_time()

    # HERE sort the_list, calling display_update every once in a while

    elapsed_time = time.process_time() - start_time

    return elapsed_time, the_list


def no_display_update(ignore_this):
    """Do no display if we are not running in TK."""
    pass


if __name__ == "__main__":
    print()
    print(sort_name)
    while True:
        print()
        in_string = input("List length: ")
        if in_string == "":
            exit()
        try:
            list_length = int(in_string)
        except Exception:
            list_length = 10
            print(f"I read that as {list_length}")
        print()

        # initialize the list with integers from 1 to list_length
        the_list = [(i+1) for i in range(list_length)]
        # now sort the list into random order
        for i in range(0, len(the_list) - 2):
            # pick a random item to the right of the_list[i]
            # and swap it with the_list[i]
            j = random.randint(i, len(the_list)-1)
            the_list[i], the_list[j] = the_list[j], the_list[i]
        if len(the_list) <= PRINT_LIMIT:
            print(the_list)

        # sort it
        elapsed_time, result = sort_list(the_list, no_display_update)
        if len(result) <= PRINT_LIMIT:
            print(result)
        print(f"Elapsed time: {elapsed_time}")

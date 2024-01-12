"""Bubble sort function."""

import time


sort_name = "BUBBLE SORT"


def sort_list(list_to_sort, display_update):
    """Sort list using Insertion Sort.

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

    for i in range(len(the_list), 1, -1):
        display_update(the_list)
        any_swaps = False
        for j in range(0, i-1):
            if the_list[j] > the_list[j+1]:
                the_list[j], the_list[j+1] =\
                    the_list[j+1], the_list[j]
                any_swaps = True
        if not any_swaps:
            break

    elapsed_time = time.process_time() - start_time

    return elapsed_time, the_list

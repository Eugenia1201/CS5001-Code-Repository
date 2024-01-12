"""Merge sort function."""

import time


sort_name = "MERGE SORT"


def sort_list(list_to_sort, display_update):
    """Sort list using Merge Sort.

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

    merge_sort(the_list, 0, len(the_list)-1, display_update)

    elapsed_time = time.process_time() - start_time

    return elapsed_time, the_list


def merge_sort(the_list, start_index, end_index, display_update):
    """Merge-sort the list from [start_index] to [end_index]."""
    # Here the start_index and end_index are BOTH included in the segment
    if end_index - start_index >= 1:

        # sort each half
        mid_index = (start_index + end_index) // 2
        merge_sort(the_list, start_index, mid_index, display_update)
        merge_sort(the_list, mid_index+1, end_index, display_update)

        # merge the halves into a new list
        outcome = []
        left = start_index
        right = mid_index + 1
        while (left <= mid_index) and (right <= end_index):
            if the_list[left] <= the_list[right]:
                outcome.append(the_list[left])
                left += 1
            else:
                outcome.append(the_list[right])
                right += 1
        # if we finished the right segment, there's stuff to get from the left
        while left <= mid_index:
            outcome.append(the_list[left])
            left += 1
        # if we finished the left segment, there's stuff to get from the right
        while right <= end_index:
            outcome.append(the_list[right])
            right += 1

        # copy the new list over the range that was just sorted
        for i in range(len(outcome)):
            the_list[start_index + i] = outcome[i]

        display_update(the_list)

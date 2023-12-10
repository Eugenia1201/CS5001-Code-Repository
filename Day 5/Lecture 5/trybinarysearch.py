"""Program to compare binary search vs. in list search performance"""

import time
import random


def binary_search(search_value):
    start_place = 0
    end_place = LIST_SIZE-1
    while start_place <= end_place:
        mid_index = (start_place + end_place) // 2
        if trial_list[mid_index] > search_value:
            end_place = mid_index - 1
        elif trial_list[mid_index] < search_value:
            start_place = mid_index + 1
        else:
            return True
    return False


def binary_search1(search_value, start_index, end_index):
    start_place = start_index
    end_place = end_index
    while start_place <= end_place:
        mid_index = (start_place + end_place) // 2
        if trial_list[mid_index] > search_value:
            end_place = mid_index - 1
        elif trial_list[mid_index] < search_value:
            start_place = mid_index + 1
        else:
            return True
    return False


def binary_search2(search_value, start_index, end_index):
    if (start_index > end_index):
        return False
    mid_index = (start_index + end_index) // 2
    if trial_list[mid_index] > search_value:
        return binary_search2(search_value, start_index, mid_index-1)
    elif trial_list[mid_index] < search_value:
        return binary_search2(search_value, mid_index+1, end_index)
    return True


def time_trial():
    start_list_time = time.process_time()
    for i in range(NUM_TRIALS):
        search_value = trial_list[random.randrange(LIST_SIZE)]
        b = (search_value in trial_list)
        if not b:
            print("Whoops!  In list error")
    end_list_time = time.process_time()
    start_binary_search1_time = time.process_time()
    for i in range(NUM_TRIALS):
        search_value = trial_list[random.randrange(LIST_SIZE)]
        b = binary_search1(search_value, 0, LIST_SIZE-1)
        if not b:
            print("Whoops!  Binary search 1 error")
    end_binary_search1_time = time.process_time()
    start_binary_search2_time = time.process_time()
    for i in range(NUM_TRIALS):
        search_value = trial_list[random.randrange(LIST_SIZE)]
        b = binary_search2(search_value, 0, LIST_SIZE-1)
        if not b:
            print("Whoops!  Binary search  2error")
    end_binary_search2_time = time.process_time()
    print(f"In list {end_list_time - start_list_time};\
 binary search 1 {end_binary_search1_time - start_binary_search1_time}\
 binary search 2 {end_binary_search2_time - start_binary_search2_time}")


NUM_TRIALS = 1000
LIST_SIZE = 1000000
VALUE_RANGE = 10000000

trial_list = sorted([random.randrange(0, VALUE_RANGE)
                     for i in range(LIST_SIZE)])
print("Starting time trial")
time_trial()

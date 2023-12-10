#

import time
import random


def time_trial(trial_list_size):
    this_trial_list = trial_list[:trial_list_size]
    mid_index = trial_list_size // 2

    start_get_first_element_time = time.process_time()
    for i in range(NUM_TRIALS):
        _ = this_trial_list[0]
    end_get_first_element_time = time.process_time()

    start_get_mid_element_time = time.process_time()
    for i in range(NUM_TRIALS):
        _ = this_trial_list[mid_index]
    end_get_mid_element_time = time.process_time()

    start_get_last_element_time = time.process_time()
    for i in range(NUM_TRIALS):
        _ = this_trial_list[-1]
    end_get_last_element_time = time.process_time()

    start_append_time = time.process_time()
    for i in range(NUM_TRIALS):
        this_trial_list.append(0)
    end_append_time = time.process_time()

    start_insert0_time = time.process_time()
    for i in range(NUM_TRIALS):
        this_trial_list.insert(0, 0)
    end_insert0_time = time.process_time()

    print(f"List size {trial_list_size}:\
     get first {end_get_first_element_time - start_get_first_element_time}\
     get mid {end_get_mid_element_time - start_get_mid_element_time}\
     get last {end_get_last_element_time - start_get_last_element_time}\
     append at end {end_append_time - start_append_time}\
     insert at beginning {end_insert0_time - start_insert0_time}")


NUM_TRIALS = 10000
LIST_SIZE = 1000000
VALUE_RANGE = 10000000

trial_list = [random.randrange(0, VALUE_RANGE) for i in range(LIST_SIZE)]

time_trial(LIST_SIZE // 100)
time_trial(LIST_SIZE // 10)
time_trial(LIST_SIZE)

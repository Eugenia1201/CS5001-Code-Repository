#

import time
import random


def time_trial(search_value, item_label):
    start_list_time = time.process_time()
    for i in range(NUM_TRIALS):
        _ = (search_value in trial_list)
    end_list_time = time.process_time()
    start_tuple_time = time.process_time()
    for i in range(NUM_TRIALS):
        _ = (search_value in trial_tuple)
    end_tuple_time = time.process_time()
    print(f"{item_label} in list {end_list_time - start_list_time};\
 in tuple {end_tuple_time - start_tuple_time}")


NUM_TRIALS = 1000000
LIST_SIZE = 1000
VALUE_RANGE = 10000000

trial_list = [random.randrange(0, VALUE_RANGE) for i in range(LIST_SIZE)]
trial_tuple = tuple(trial_list)

print("UNSORTED")
time_trial(trial_list[0], "First")
time_trial(trial_list[LIST_SIZE//2], "Mid")
time_trial(trial_list[-1], "Last")

trial_list.sort()
trial_tuple = tuple(trial_list)

print("SORTED")
time_trial(trial_list[0], "First")
time_trial(trial_list[LIST_SIZE//2], "Mid")
time_trial(trial_list[-1], "Last")

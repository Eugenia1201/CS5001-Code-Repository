"""Validating input from console
(with two flag variables used)"""


def get_integer(prompt_string, min_value=None, max_value=None):
    keep_asking = True
    while keep_asking:
        input_string = input(prompt_string)
        if input_string == "":
            result = None
            keep_asking = False
        else:
            try:
                int_value = int(input_string)
                if ((min_value is None) or (int_value >= min_value)) and \
                   ((max_value is None) or (int_value <= max_value)):
                    result = int_value
                    # Only stop asking when we get a valid int_value
                    keep_asking = False
                else:
                    # later in the main program when call get_ingeter(),
                    # selectively passing in whether min_value or max_value
                    if min_value is None:
                        print(f"Must be no greater than {max_value}")
                    elif max_value is None:
                        print(f"Must be no less than {min_value}")
                    else:
                        print(f"Must be between{min_value} and {max_value}")
            except ValueError:
                print("Must be an integer")
    return result


keep_going = True
while keep_going:
    i1 = get_integer("Give me a number:")
    keep_going = (i1 is not None)
    if keep_going:
        i2 = get_integer("Give me number from 1 to 10: ", 1, 10)
        keep_going = (i2 is not None)
    if keep_going:
        i3 = get_integer("Give me number 1 or greater: ", 1)
        keep_going = (i3 is not None)
    if keep_going:
        i4 = get_integer("Give me number no greater than 10: ", max_value=10)
        keep_going = (i4 is not None)
    if keep_going:
        print(f"I got {i1}, {i2}, {i3}, and {i4}")
        print()

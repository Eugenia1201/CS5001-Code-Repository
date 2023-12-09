"""Validating input from console"""


def is_integer(input_string, min_int, max_int):
    try:
        int_value = int(input_string)
        result = int_value if min_int <= int_value <= max_int else None
    except (ValueError, TypeError):
        result = None
    return result


def is_integer2(input_string, min_value=None, max_value=None):
    try:
        int_value = int(input_string)
        if ((min_value is None) or (int_value >= min_value)) and \
           ((max_value is None) or (int_value <= max_value)):
            result = int_value
    except ValueError:
        result = None
    return result


while (input_line := input("Give me a numebr from 1 to 10: ")) != "":
    if is_integer(input_line, 1, 10):
        print("That's a good number!")
    else:
        print("Please follow instructions.")

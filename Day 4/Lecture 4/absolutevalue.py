""" Some ways to define absolute value

NOTE:  There should be docstrings, they're omitted to make the code clearer
        for class discussion

FOR DISCUSSION:  Compare #2,3,4,5 with #1
"""


def absolute_value_1(x):
    if x < 0:
        return -x
    else:
        return x


def absolute_value_2(x):
    if x < 0:
        return -x
    elif x > 0:
        return x


def absolute_value_3(x):
    if x < 0:
        return -x
    return x


def absolute_value_4(x):
    return x if x >= 0 else -x


def absolute_value_5(x):
    answer = x if x >= 0 else -x
    return answer

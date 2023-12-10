""" Day 9 homework - Kaiqi Zhang """


class TooBigError(ValueError):
    pass


def pow(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    if a > 10 or b > 10:
        raise TooBigError
    else:
        return a ** b


def number_or_none(s):
    s = input(("please enter a number: "))
    try:
        return float(s)
    except ValueError:
        return None


if __name__ == "__main__":
    a = int(input("please type in the number 'a': "))
    b = int(input("please type in the number 'b': "))

    try:
        result = pow(a, b)
        print(f"The result of {a} raised to the power of {b} is {result}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except TooBigError as tbe:
        print(f"Error: {tbe}")

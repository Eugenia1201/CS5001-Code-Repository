""" Some ways to define square root using Newton's method

FOR DISCUSSION:
    Why use * 0.5 instead of / 2.0 ?
Compare #2 with #1
"""

import math


def square_root_1(x, tolerance):

    # starting guess is x/2
    current_guess = x * 0.5
    next_guess = (current_guess + (x / current_guess)) * 0.5

    while abs(current_guess - next_guess) > tolerance:
        current_guess = next_guess
        next_guess = (current_guess + (x / current_guess)) * 0.5

    return next_guess


def square_root_2(x, tolerance):

    # starting guess is x/2
    current_guess = x * 0.5

    while True:
        next_guess = (current_guess + (x / current_guess)) * 0.5
        if abs(current_guess - next_guess) <= tolerance:
            return next_guess
        current_guess = next_guess


def try_square_roots(x, tolerance):
    print(f"Square root of {x}\t{math.sqrt(x)}\t{square_root_1(x, tolerance)}")


try_square_roots(2.0, 0.000001)
try_square_roots(4.0, 0.1)
try_square_roots(9.0, 0.1)
try_square_roots(10.0, 0.1)

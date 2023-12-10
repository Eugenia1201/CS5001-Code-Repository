""" file for trying stuff out """

import sys
import math


def my_abs(val):
    """  absolute value

    Args:
        val (integer): the value I want
    """
    if val < 0:
        val = -val
    print(val)


print(type(3))
print(type(2.5))
print(type(3 * 2.5))
print(type(4 / 2))
print(type(4 / 3))
print(type(5 // 3))
print(type(5 % 3))
print(type(4.5 / 1.5))

print(5 / 3)

print(5 // 3)

print(5 % 3)

print(4.5 / 1.5)

print(2.5e-1)

print(2.5 ** 1.3)

print(0.1)
print(1.0 - 0.9)

print(abs(-2))

print(round(12.34, 1))
print(round(123.4565, 3))

print(sys.maxsize)
print(math.pi)
print(math.isclose(3.51, 3.52, abs_tol=0.1))

my_abs(3)
my_abs(-4)

print(int(True))

is_bigger = (4 > 3)
print(is_bigger)

x = 3
in_range = 2 < (x < 4)
print(in_range)

x = 10
print(x << 1, x >> 2)  # Convert ints to binaries first then perform
y = 6
print(x & y, x | y, x ^ y)  # bitwise operation but still return ints
y &= x
print(y)

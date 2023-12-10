"""Program to compare iterative vs. recursive approach to compute factorials"""


import time


def factorial1(n):
    result = 1
    for i in range(n):
        result *= (1 + i)
    return result


def factorial2(n):
    result = 1 if (n == 1) else (n * factorial2(n-1))
    return result


TARGET = 200
ITERATIONS = 100000

print(f"1:{factorial1(1)}   3:{factorial1(3)}   5:{factorial1(5)}")
start_time = time.process_time()
for i in range(ITERATIONS):
    x = factorial1(TARGET)
end_time = time.process_time()
print(f"Factorial1: {ITERATIONS} x factorial({TARGET}):\
 {end_time - start_time} sec")

print(f"1:{factorial2(1)}   3:{factorial2(3)}   5:{factorial2(5)}")
start_time = time.process_time()
for i in range(ITERATIONS):
    x = factorial2(TARGET)
end_time = time.process_time()
print(f"Factorial2: {ITERATIONS} x factorial({TARGET}):\
 {end_time - start_time} sec")

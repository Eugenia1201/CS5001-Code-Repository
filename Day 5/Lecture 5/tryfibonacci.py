"""program to compare iterative vs. recursive approach to compute fibonacci"""


import time


def fibonacci1(n):
    if n == 1:
        result = 0
    elif n == 2:
        result = 1
    else:
        result = fibonacci1(n-1) + fibonacci1(n-2)
    return result


def fibonacci2(n):
    if n == 1:
        result = 0
    elif n == 2:
        result = 1
    else:
        beforelast = 0
        last = 1
        for i in range(3, n+1):
            result = last + beforelast
            beforelast = last
            last = result
    return result


TARGET = 30
ITERATIONS = 100

print(f"1:{fibonacci1(1)}   3:{fibonacci1(3)}   5:{fibonacci1(5)}")
start_time = time.process_time()
for i in range(ITERATIONS):
    x = fibonacci1(TARGET)
end_time = time.process_time()
print(f"Fibonacci1: {ITERATIONS} of Fibonacci({TARGET}):\
 {end_time - start_time} sec")

TARGET = 100000

print(f"1:{fibonacci2(1)}   3:{fibonacci2(3)}   5:{fibonacci2(5)}")
start_time = time.process_time()
for i in range(ITERATIONS):
    x = fibonacci2(TARGET)
end_time = time.process_time()
print(f"Fibonacci2: {ITERATIONS} x Fibonacci({TARGET}):\
 {end_time - start_time} sec")

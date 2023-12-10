"Prime Number Printer"

import time
import math

# ask the user how many primes to print

number_to_print = int(input("How many primes do you want? "))

# print that many primes

start_time = time.process_time()
primes = []

# special-case 2 and 3

if (number_to_print) > 0:
    primes.append(2)
if (number_to_print) > 1:
    primes.append(3)

candidate = 3

for how_many_printed in range(2, number_to_print):

    # print the next prime number

    is_it_prime = False

    while (not is_it_prime):
        # consider next candidate
        candidate += 2

        # set is_it_prime to tell whether candidate is prime
        is_it_prime = True
        candidate_square_root = math.ceil(math.sqrt(candidate))
        for divisor in primes:
            if (candidate % divisor) == 0:
                is_it_prime = False
                break
            if (divisor > candidate_square_root):
                break

    primes.append(candidate)

end_time = time.process_time()
elapsed_time = end_time - start_time

# print(primes)
print("Elapsed time is ", elapsed_time)

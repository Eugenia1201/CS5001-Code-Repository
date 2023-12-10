"""Useing functions to generate a list of n primes"""


def is_prime(num):
    if num < 2:
        return False
    # Only need to check up to the square root of num
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def main():
    try:
        n = int(input("Enter the value of n: "))
        if n <= 0:
            print("Please enter a positive integer")
        else:
            prime_list = generate_primes(n)
            print(f"the first {n} prime numbers are: {prime_list}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")


if __name__ == "__main__":
    main()

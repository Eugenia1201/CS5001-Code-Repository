"""Recursive approach to compute GCD"""


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif b == 0:
        return (a)
    return gcd(b, a % b)


print(f"GCD(49,35) = {gcd(49, 35)}")

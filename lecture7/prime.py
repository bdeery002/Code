# A prime number is a natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself.
import math

def is_prime(n):
    # Check if n is less than 2, which are not prime numbers.
    if n <2:
        return False
    # Check for factors from 2 to the square root of n.
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
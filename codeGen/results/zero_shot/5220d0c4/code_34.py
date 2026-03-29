import sys
from math import sqrt

def sieve_of_eratosthenes(n):
    # Generate all prime numbers up to n
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [p for p in range(2, n + 1) if primes[p]]

def find_min_prime_divisor(n, bad_primes):
    # Find the minimum prime divisor of n
    min_prime_divisor = None
    for p in bad_primes:
        if n % p == 0:
            return p
    for p in range(2, int(sqrt(n)) + 1):
        if n % p == 0 and p not in bad_primes:
            return p
    return min_prime_divisor

def calculate_beauty(n, min_prime_divisor):
    # Calculate the beauty of the number n based on its minimum prime divisor
    if min_prime_divisor is None or min_prime_divisor not in bad_primes:
        return 1
    else:
        return -1

def find_max_beauty(array, bad_primes):
    max_beauty = 0
    for n in array:
        min_prime_divisor = find_min_prime_divisor(n, bad_primes)
        beauty = calculate_beauty(n, min_prime_divisor)
        if beauty > max_beauty:
            max_beauty = beauty
    return max_beauty

# Read input from standard input
n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

# Calculate and print the maximum beauty
max_beauty = find_max_beauty(array, bad_primes)
print(max_beauty)

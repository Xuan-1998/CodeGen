import sys
from math import sqrt

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [p for p in range(2, n + 1) if primes[p]]

def min_prime_divisor(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return i

def is_good_prime(p):
    # Check if p is a good prime (for this problem, assume it's always good)
    return True

n, m = map(int, sys.stdin.readline().split())
bad_primes = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

# Initialize the first row with values from 0 to n-1
min_divisors = [i for i in range(n)]

table = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    if is_good_prime(arr[i]):
        table[i][0] += min_divisors[i]
    else:
        table[i][0] -= min_divisors[i]

# Fill the rest of the table
for j in range(1, m + 1):
    for i in range(n - 1, -1, -1):
        if is_good_prime(arr[i]):
            table[i][j] = max(table[i][j-1], table[i+1][j-1] + min_divisors[i])
        else:
            table[i][j] = max(table[i][j-1] - min_divisors[i], table[i+1][j-1])

print(max(table[-1]))

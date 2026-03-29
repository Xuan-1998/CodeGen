import sys
from collections import defaultdict

def sieve_of_eratosthenes(n_max):
    sieve = [True] * (n_max + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int((n_max ** 0.5)) + 1):
        if sieve[i]:
            for j in range(i * i, n_max + 1, i):
                sieve[j] = False
    return [p for p in range(2, n_max + 1) if sieve[p]]

def prime_permutations_count(p):
    factorial = 1
    for digit in str(p):
        factorial *= int(digit)
    return factorial // (reduce(lambda x, y: x * y, map(int, str(p))))

def solve(n_max, k_perms):
    primes = sieve_of_eratosthenes(n_max)
    dp = defaultdict(bool)
    for p in primes:
        if prime_permutations_count(p) == k_perms:
            dp[p] = True
    count = 0
    smallest = float('inf')
    largest = -float('inf')
    for p, is_prime in dp.items():
        if is_prime:
            count += 1
            smallest = min(smallest, p)
            largest = max(largest, p)
    return [count, smallest, largest]

n_max, k_perms = map(int, input().split())
print(*solve(n_max, k_perms))

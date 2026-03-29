import sys
from itertools import permutations

def generate_primes(n_max):
    # Sieve of Eratosthenes to generate all prime numbers up to n_max
    primes = [True] * (n_max + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n_max ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n_max + 1, i):
                primes[j] = False
    return [i for i in range(2, n_max + 1) if primes[i]]

def count_prime_permutations(n):
    # Generate all possible permutations of the digits of n
    perms = set(int("".join(map(str, p))) for p in permutations(str(n)))
    # Check if each permutation is prime
    return sum(1 for _ in filter(lambda x: x > 1 and all(y < x for y in range(2, int(x ** 0.5) + 1))), perms)

def solve(n_max, k_perms):
    primes = generate_primes(n_max)
    count = 0
    smallest = largest = 0
    for p in primes:
        if count_prime_permutations(p) == k_perms:
            count += 1
            smallest = min(smallest, p)
            largest = max(largest, p)
    return [count, smallest, largest]

n_max, k_perms = map(int, sys.stdin.readline().split())
print(solve(n_max, k_perms))

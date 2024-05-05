import itertools
from collections import OrderedDict

def sieve_of_eratosthenes(n_max):
    # Generate all prime numbers up to n_max using Sieve of Eratosthenes
    primes = [True] * (n_max + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n_max ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n_max + 1, i):
                primes[j] = False
    return [p for p in range(2, n_max + 1) if primes[p]]

def count_permutations(prime_number):
    # Generate all permutations of the digits of a prime number
    digits = str(prime_number)
    perms = set()
    def permute(digits):
        if len(digits) == 1:
            perms.add(int(digits))
        else:
            for i in range(len(digits)):
                rest = digits[:i] + digits[i+1:]
                yield from permute(rest + [digits[i]])
    return list(permute(digits))

def solve(n_max, k_perms):
    # Count prime numbers with exactly k_perms permutations
    primes = sieve_of_eratosthenes(n_max)
    prime_perm_counts = OrderedDict()
    for prime in primes:
        perms = count_permutations(prime)
        perms_count = len(perms)
        if perms_count == k_perms:
            prime_perm_counts[prime] = perms_count

    # Find the smallest and largest prime numbers with exactly k_perms permutations
    smallest_prime = max_prime = None
    for prime, _ in prime_perm_counts.items():
        if smallest_prime is None or prime < smallest_prime:
            smallest_prime = prime
        if max_prime is None or prime > max_prime:
            max_prime = prime

    # Return the count and the smallest and largest prime numbers
    return [len(prime_perm_counts), smallest_prime, max_prime]

# Read input from stdin
n_max, k_perms = map(int, input().split())

# Solve and print output to stdout
print(solve(n_max, k_perms))

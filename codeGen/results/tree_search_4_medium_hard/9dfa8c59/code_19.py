import sys

def sieve_of_eratosthenes(n_max):
    sieve = [True] * (n_max + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n_max ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n_max + 1, i):
                sieve[j] = False
    return [p for p in range(2, n_max + 1) if sieve[p]]

def count_permutations(n, k_perms):
    unique_digits = set()
    for digit in str(n):
        unique_digits.add(int(digit))
    return len(unique_digits) == k_perms

n_max, k_perms = map(int, sys.stdin.readline().split())
prime_numbers = sieve_of_eratosthenes(n_max)
prime_permutations = 0
min_prime = max_prime = 0

for prime in prime_numbers:
    if count_permutations(prime, k_perms):
        prime_permutations += 1
        min_prime = min(min_prime, prime)
        max_prime = max(max_prime, prime)

if prime_permutations == 0:
    print([0, 0, 0])
else:
    print([prime_permutations, min_prime, max_prime])

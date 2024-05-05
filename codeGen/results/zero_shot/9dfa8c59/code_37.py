import sys

n_max, k_perms = map(int, input().split())
if k_perms < 1 or k_perms > 3:
    print([0, 0, 0])
    sys.exit()

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

primes_up_to_n_max = sieve_of_eratosthenes(n_max)

def count_prime_permutations(prime, k_perms):
    permutations = set()
    for p in str(prime):
        for i in range(len(p)):
            permutation = int(''.join(sorted([p[i]] + [c for c in p if c != p[i]]))))
            permutations.add(permutation)
    return len(permutations) == k_perms

count = sum(1 for prime in primes_up_to_n_max if count_prime_permutations(prime, k_perms))

smallest = largest = None
for prime in primes_up_to_n_max:
    if count_prime_permutations(prime, k_perms):
        if smallest is None or prime < smallest:
            smallest = prime
        if largest is None or prime > largest:
            largest = prime

print([count, smallest, largest])

import sys
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_prime_permutations(prime_num):
    prime_perm_count = 0
    for p in permutations(str(prime_num)):
        perm = int(''.join(map(str, p)))
        if is_prime(perm):
            prime_perm_count += 1
    return prime_perm_count

n_max = int(input())
k_perms = int(input())

primes = [i for i in range(2, n_max+1) if is_prime(i)]

prime_counts = []
smallest_prime = None
largest_prime = None

for p in primes:
    perm_count = count_prime_permutations(p)
    if perm_count == k_perms:
        prime_counts.append(p)
        smallest_prime = min((p, smallest_prime), key=None) if smallest_prime is None else (p, smallest_prime)[1]
        largest_prime = max((p, largest_prime), key=None) if largest_prime is None else (p, largest_prime)[1]

print([len(prime_counts), smallest_prime, largest_prime])

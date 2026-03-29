from collections import Counter
import math

def get_prime_permutations(n):
    count = Counter(str(n))
    permutations = set()
    for p in range(10**len(str(n))):
        if Counter(str(p)) == count:
            permutations.add(p)
    return len(permutations)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

n_max, k_perms = map(int, input().split())

count = 0
smallest_prime = float('inf')
largest_prime = 0

for i in range(2, n_max):
    if is_prime(i) and get_prime_permutations(i) == k_perms:
        count += 1
        smallest_prime = min(smallest_prime, i)
        largest_prime = max(largest_prime, i)

print([count, smallest_prime, largest_prime])

from itertools import permutations
import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_permutations(n):
    perms = set(str(p) for p in permutations(str(n)))
    prime_perms = sum(1 for perm in perms if is_prime(int(perm)))
    return prime_perms, min(map(int, perms)), max(map(int, perms))

n_max, k_perms = map(int, input().split())
counts = {}
for num in range(2, n_max):
    if is_prime(num):
        count, min_perm, max_perm = count_permutations(num)
        if count == k_perms:
            counts[num] = (count, min_perm, max_perm)

print(len(counts), *min(counts.values(), key=lambda x: x[1]), sep='\n')

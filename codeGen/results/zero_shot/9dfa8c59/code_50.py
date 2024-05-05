import sys
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_permutations(n):
    digits = [int(d) for d in str(n)]
    perms = set(permutations(digits))
    count = sum(is_prime(int(''.join(map(str, p)))) for p in perms)
    return count

n_max = int(sys.stdin.readline().strip())
k_perms = int(sys.stdin.readline().strip())

count = 0
min_num = float('inf')
max_num = -1

for n in range(2, n_max):
    if is_prime(n):
        perms_count = prime_permutations(n)
        if perms_count == k_perms:
            count += 1
            min_num = min(min_num, n)
            max_num = max(max_num, n)

print([count, min_num, max_num])

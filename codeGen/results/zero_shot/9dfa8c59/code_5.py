from itertools import permutations
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n_max = int(input())
k_perms = int(input())

count = 0
min_prime = float('inf')
max_prime = -float('inf')

for num in range(2, n_max):
    if is_prime(num):
        perms = set([''.join(p) for p in permutations(str(num))])
        if len(perms) == k_perms:
            count += 1
            min_prime = min(min_prime, num)
            max_prime = max(max_prime, num)

print([count, min_prime, max_prime] if count > 0 else [0, 0, 0])

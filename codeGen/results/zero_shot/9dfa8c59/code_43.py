import sys
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n_max = int(sys.stdin.readline())
k_perms = int(sys.stdin.readline())

count = 0
smallest = float('inf')
largest = -float('inf')

for i in range(2, n_max):
    if is_prime(i):
        perms = set(permutations(str(i)))
        if len(perms) == k_perms:
            count += 1
            smallest = min(smallest, i)
            largest = max(largest, i)

print([count, smallest, largest])

import sys
from itertools import permutations

# Read input from stdin
n_max, k_perms = map(int, sys.stdin.readline().split())

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_nums = [i for i in range(2, n_max+1) if is_prime(i)]

count = 0
smallest = float('inf')
largest = -float('inf')

for prime in prime_nums:
    perms_count = len(set(int(''.join(map(str, p))) for p in permutations(str(prime))))
    if perms_count == k_perms:
        count += 1
        smallest = min(smallest, prime)
        largest = max(largest, prime)

print([count, smallest, largest])

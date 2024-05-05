import sys
from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_permutations_count(n_max, k_perms):
    count = 0
    smallest = float('inf')
    largest = 0
    for n in range(2, n_max+1):
        if is_prime(n):
            perms = set(permutations(map(int, str(n))))
            if len(perms) == k_perms:
                count += 1
                smallest = min(smallest, n)
                largest = max(largest, n)
    return [count, smallest, largest]

n_max = int(sys.stdin.readline().strip())
k_perms = int(sys.stdin.readline().strip())

print(prime_permutations_count(n_max, k_perms))

from itertools import permutations
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

n_max, k_perms = map(int, input().split())
count = 0
smallest = largest = None

for i in range(2, n_max):
    if is_prime(i):
        perms = set([''.join(p) for p in permutations(str(i))])
        if len(perms) == k_perms:
            count += 1
            if smallest is None or i < smallest:
                smallest = i
            if largest is None or i > largest:
                largest = i

print([count, smallest, largest] if (smallest and largest) else [0, 0, 0])

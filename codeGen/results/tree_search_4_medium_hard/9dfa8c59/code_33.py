import sys
from collections import defaultdict

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_permutations(n):
    # Count the number of permutations by rearranging digits
    perms = set()
    for p in prime_perms[n]:
        perms.add(''.join(sorted(str(p))))
    return len(perms)

n_max, k_perms = map(int, sys.stdin.readline().split())
prime_nums = set()
prime_perms = defaultdict(set)
count = 0
smallest = None
largest = None

for i in range(2, n_max + 1):
    if is_prime(i):
        prime_nums.add(i)
        for p in prime_perms[i]:
            perms = count_permutations(p)
            if perms == k_perms:
                count += 1
                if smallest is None or p < smallest:
                    smallest = p
                if largest is None or p > largest:
                    largest = p

print([count, smallest, largest])

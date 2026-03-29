import sys

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def count_prime_permutations(n):
    permutations = set()
    for p in str(n):
        permutations.add(int(''.join(sorted(p))))
    return sum(1 for p in permutations if is_prime(p))

n_max = int(sys.stdin.readline())
k_perms = int(sys.stdin.readline())

prime_count = 0
smallest_prime = float('inf')
largest_prime = float('-inf')

for i in range(2, n_max):
    if is_prime(i) and count_prime_permutations(i) == k_perms:
        prime_count += 1
        smallest_prime = min(smallest_prime, i)
        largest_prime = max(largest_prime, i)

print([prime_count, smallest_prime, largest_prime])

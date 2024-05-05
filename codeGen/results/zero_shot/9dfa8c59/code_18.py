import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_permutations(n):
    permutations = set()
    for p in str(n):
        for p_ in sorted(str(n).replace(p, '')):
            permutations.add(int(''.join([p, p_, p])))
    return len(set(map(int, permutations)))

n_max = int(sys.stdin.readline())
k_perms = int(sys.stdin.readline())

count = 0
min_prime = float('inf')
max_prime = -1

for i in range(2, n_max + 1):
    if is_prime(i) and prime_permutations(i) == k_perms:
        count += 1
        min_prime = min(min_prime, i)
        max_prime = max(max_prime, i)

print([count, min_prime, max_prime])

import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def permutations(n):
    digits = [int(d) for d in str(n)]
    return list(itertools.permutations(digits))

n_max, k_perms = map(int, input().split())
count = 0
smallest = float('inf')
largest = 0

for i in range(2, n_max + 1):
    if is_prime(i):
        perms = permutations(str(i))
        if len([p for p in perms if is_prime(int(''.join(map(str, p))))]) == k_perms:
            count += 1
            smallest = min(smallest, i)
            largest = max(largest, i)

print([count, smallest, largest])

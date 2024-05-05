import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def permute_digits(n):
    digits = [int(d) for d in str(n)]
    perms = list(itertools.permutations(digits))
    prime_perms = []
    for p in perms:
        perm = int(''.join(map(str, p)))
        if is_prime(perm):
            prime_perms.append(perm)
    return set(prime_perms)

n_max, k_perms = map(int, input().split())
count = 0
smallest = float('inf')
largest = float('-inf')

for i in range(2, n_max + 1):
    if is_prime(i) and len(permute_digits(i)) == k_perms:
        count += 1
        smallest = min(smallest, i)
        largest = max(largest, i)

print([count, smallest, largest])

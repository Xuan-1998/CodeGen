n_max = int(input())
k_perms = int(input())

count = 0
min_prime = float('inf')
max_prime = float('-inf')

for n in range(2, n_max):
    if is_prime(n):
        perms = prime_permutations(n)
        if len(perms) == k_perms:
            count += 1
            min_prime = min(min_prime, n)
            max_prime = max(max_prime, n)

print([count, min_prime, max_prime])

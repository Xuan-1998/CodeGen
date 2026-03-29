count = 0
min_prime = float('inf')
max_prime = 0

for i in range(2, n_max):
    if is_prime(i):
        perms = permute_digits(i)
        if len(set(perms)) == k_perms:  # check if there are exactly k_perms unique permutations
            count += 1
            min_prime = min(min_prime, i)
            max_prime = max(max_prime, i)

print([count, min_prime, max_prime])

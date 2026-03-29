n_max = int(input())
k_perms = int(input())

result = prime_permutations(n_max, k_perms)
print(*result, sep=", ")

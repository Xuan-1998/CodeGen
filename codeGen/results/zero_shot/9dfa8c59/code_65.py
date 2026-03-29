import sys
import itertools

n_max = int(sys.stdin.readline())
k_perms = int(sys.stdin.readline())

prime_numbers = sieve_of_eratosthenes(n_max)
result = count_prime_permutations(prime_numbers, k_perms)

print(*result)

import sys

n_max, k_perms = map(int, sys.stdin.readline().split())
primes = find_primes(n_max)
result = count_k_perms_primes(primes, k_perms)

print(result)

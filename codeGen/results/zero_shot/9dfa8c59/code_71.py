n_max, k_perms = map(int, input().split())
primes = sieve_of_eratosthenes(n_max)
output = count_prime_numbers_with_k_perms(k_perms, primes)
print(*output, sep=', ')

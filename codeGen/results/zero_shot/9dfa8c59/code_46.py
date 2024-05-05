n_max, k_perms = map(int, input().split())

prime_numbers = sieve_of_eratosthenes(n_max)

count = count_prime_numbers_with_k_perms(prime_numbers)

if count == 0:
    result = [0, 0, 0]
else:
    smallest_prime_number = min([p for p in prime_numbers if count_prime_numbers_with_k_perms([p]) == k_perms])
    largest_prime_number = max([p for p in prime_numbers if count_prime_numbers_with_k_perms([p]) == k_perms])
    result = [count, smallest_prime_number, largest_prime_number]

print(*result)

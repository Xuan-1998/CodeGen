def find_prime_numbers_with_k_perms(n_max, k_perms):
    count = 0
    smallest_prime = float('inf')
    largest_prime = 0

    for prime_number in prime_numbers:
        perms_count = count_prime_permutations(prime_number)
        if perms_count == k_perms:
            count += 1
            smallest_prime = min(smallest_prime, prime_number)
            largest_prime = max(largest_prime, prime_number)

    return [count, smallest_prime, largest_prime]

k_perms = int(input())
result = find_prime_numbers_with_k_perms(n_max, k_perms)
print(result)

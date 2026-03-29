def solve(n_max, k_perms):
    count = 0
    min_prime = float('inf')
    max_prime = float('-inf')

    for prime in primes_up_to_n_max:
        if count_prime_permutations(prime, k_perms):
            count += 1
            min_prime = min(min_prime, prime)
            max_prime = max(max_prime, prime)

    return [count, min_prime, max_prime]

print(solve(int(input()), int(input())))

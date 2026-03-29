def solve(n_max, k_perms):
    primes = generate_primes(n_max)
    count = 0
    smallest = float('inf')
    largest = -1
    for prime in primes:
        if count_prime_perms(prime, k_perms) == k_perms:
            count += 1
            if prime < smallest:
                smallest = prime
            if prime > largest:
                largest = prime
    return [count, smallest, largest]

n_max, k_perms = map(int, input().split())
print(solve(n_max, k_perms))

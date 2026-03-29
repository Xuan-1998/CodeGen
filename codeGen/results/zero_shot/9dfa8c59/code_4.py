import itertools
from sympy import isprime

def solve(n_max, k_perms):
    # Generate all prime numbers up to n_max
    primes = [i for i in range(2, n_max) if isprime(i)]

    count = 0
    min_prime = float('inf')
    max_prime = float('-inf')

    for prime in primes:
        # Generate permutations of the prime number's digits
        perms = [''.join(p) for p in itertools.permutations(str(prime))]

        # Count the number of prime permutations
        prime_perms_count = sum(1 for perm in perms if isprime(int(perm)))

        if prime_perms_count == k_perms:
            count += 1
            min_prime = min(min_prime, int(perm) for perm in perms)
            max_prime = max(max_prime, int(perm) for perm in perms)

    return [count, min_prime, max_prime]

# Read input from stdin
n_max, k_perms = map(int, input().split())

# Print output to stdout
print(solve(n_max, k_perms))

import math
from collections import Counter

def count_prime_permutations(n_max, k_perms):
    # Generate all prime numbers up to n_max using Sieve of Eratosthenes
    sieve = [True] * (n_max + 1)
    for i in range(2, int(math.sqrt(n_max)) + 1):
        if sieve[i]:
            for j in range(i*i, n_max + 1, i):
                sieve[j] = False

    prime_count = 0
    min_prime = float('inf')
    max_prime = float('-inf')

    # Iterate over each prime number p:
    for p in range(2, n_max + 1):
        if not sieve[p]:
            continue

        # Calculate the total number of permutations using the formula
        num_permutations = math.factorial(p)
        for digit in str(p):
            num_permutations //= math.factorial(int(digit))

        if num_permutations == k_perms:
            prime_count += 1
            min_prime = min(min_prime, p)
            max_prime = max(max_prime, p)

    return [prime_count, min_prime, max_prime]


# Test the function with inputs from stdin
n_max, k_perms = map(int, input().split())
print(count_prime_permutations(n_max, k_perms))

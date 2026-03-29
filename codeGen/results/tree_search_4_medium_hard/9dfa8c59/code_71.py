import sys
from itertools import permutations

# Read input from standard input
n_max, k_perms = map(int, input().split())

# Generate all prime numbers up to n_max
def generate_primes(n):
    primes = []
    for p in range(2, n + 1):
        is_prime = True
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(p)
    return primes

primes = generate_primes(n_max)

# Initialize dynamic programming table and variables
dp_table = {}
count = 0
smallest = float('inf')
largest = 0

for p in primes:
    # Convert prime number to a string of digits
    str_p = str(p)
    # Generate all permutations of the digits
    perms = [''.join(p) for p in permutations(str_p)]
    # Count the number of permutations that are less than or equal to k_perms
    perms_count = len([p for p in perms if int(p) <= k_perms])
    # Update dynamic programming table and variables
    dp_table[p] = perms_count
    if perms_count <= k_perms:
        count += 1
        smallest = min(smallest, p)
        largest = max(largest, p)

# Print output to standard output
print([count, smallest, largest])

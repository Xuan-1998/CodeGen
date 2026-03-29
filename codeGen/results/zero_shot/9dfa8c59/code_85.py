import sys

# Read input from stdin
n_max = int(sys.stdin.readline())
k_perms = int(sys.stdin.readline())

# Sieve of Eratosthenes algorithm to count prime numbers
primes = [True] * (n_max + 1)
primes[0] = primes[1] = False
for i in range(2, int(n_max ** 0.5) + 1):
    if primes[i]:
        for j in range(i * i, n_max + 1, i):
            primes[j] = False

# Count prime numbers with k_perms prime permutations
count = 0
smallest_prime = largest_prime = None
for p in range(2, n_max + 1):
    if primes[p]:
        # Generate all possible permutations of the digits of the prime number
        perms = set()
        for perm in itertools.permutations(str(p)):
            num = int("".join(map(str, perm)))
            if primes[num] and len([i for i in range(2, n_max) if primes[i]]) == k_perms:
                count += 1
                if smallest_prime is None or p < smallest_prime:
                    smallest_prime = p
                if largest_prime is None or p > largest_prime:
                    largest_prime = p

# Print output to stdout
print(count, smallest_prime, largest_prime)

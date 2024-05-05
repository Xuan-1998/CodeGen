import itertools

def sieve_of_eratosthenes(n_max):
    primes = [True] * (n_max + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n_max ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n_max + 1, i):
                primes[j] = False
    return [i for i in range(n_max + 1) if primes[i]]

def prime_permutations(n):
    digits = [int(x) for x in str(n)]
    perms = list(itertools.permutations(digits))
    return [int(''.join(map(str, p))) for p in perms]

def solve(n_max, k_perms):
    primes = sieve_of_eratosthenes(n_max)
    count = 0
    smallest = largest = 0
    for prime in primes:
        if len([p for p in prime_permutations(prime) if p in primes]) == k_perms:
            count += 1
            smallest = min(smallest, prime)
            largest = max(largest, prime)
    return [count, smallest, largest]

# Read input from stdin
n_max, k_perms = map(int, input().split())

# Solve the problem
result = solve(n_max, k_perms)

# Print the result to stdout
print(*result, sep=' ')

import itertools

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [p for p in range(2, n + 1) if sieve[p]]

def prime_permutations(p):
    digits = [int(d) for d in str(p)]
    perms = set(int(''.join(map(str, perm))) for perm in itertools.permutations(digits))
    count = sum(1 for perm in perms if perm in sieve_of_eratosthenes(min(p, 10000)))
    return count

def solve(n_max, k_perms):
    primes = sieve_of_eratosthenes(n_max)
    count = 0
    smallest = largest = None
    for p in primes:
        perms_count = prime_permutations(p)
        if perms_count == k_perms:
            count += 1
            if smallest is None or p < smallest:
                smallest = p
            if largest is None or p > largest:
                largest = p
    return [count, smallest, largest]

n_max, k_perms = map(int, input().split())
print(solve(n_max, k_perms))

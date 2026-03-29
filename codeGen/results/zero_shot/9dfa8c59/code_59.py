import itertools

def generate_primes(n_max):
    primes = [True] * (n_max + 1)
    primes[0] = primes[1] = False
    for i in range(2, int((n_max + 1) ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n_max + 1, i):
                primes[j] = False
    return [i for i in range(n_max + 1) if primes[i]]

def prime_permutations(n):
    digits = [int(x) for x in str(n)]
    perms = set()
    for p in itertools.permutations(digits):
        perm = int(''.join(map(str, p)))
        if perm != n and is_prime(perm):
            perms.add(perm)
    return len(perms)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int((n + 1) ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n_max, k_perms = map(int, input().split())
primes = generate_primes(n_max)
count = sum(1 for p in primes if prime_permutations(p) == k_perms)
smallest_prime = min([p for p in primes if prime_permutations(p) == k_perms])
largest_prime = max([p for p in primes if prime_permutations(p) == k_perms])

print(count, smallest_prime, largest_prime)

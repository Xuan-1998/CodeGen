def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [p for p in range(n + 1) if primes[p]]

def count_prime_permutations(p):
    perms = set()
    for i in range(len(str(p))):
        for j in range(i + 1, len(str(p)) + 1):
            perm = int("".join(sorted(str(p)[i:j]))[::])
            if is_prime(perm):
                perms.add(perm)
    return len(perms)

n_max = int(input())
k_perms = int(input())

primes = sieve_of_eratosthenes(n_max)
prime_permutations = [count_prime_permutations(p) for p in primes]

count = sum(1 for p in prime_permutations if p == k_perms)
smallest = min([p for p, cp in zip(primes, prime_permutations) if cp == k_perms])
largest = max([p for p, cp in zip(primes, prime_permutations) if cp == k_perms])

print([count, smallest, largest])

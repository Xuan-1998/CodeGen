import sys

def prime_permutations(n_max, k_perms):
    primes = set()
    for i in range(2, n_max + 1):
        if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
            primes.add(i)

    prime_counts = {}
    for p in primes:
        perms = sorted(set(int(''.join(sorted(str(p)))) for _ in range(k_perms)))
        if len(perms) == k_perms:
            prime_counts[p] = len(perms)

    min_prime, max_prime = 0, 0
    for p, count in prime_counts.items():
        if count >= k_perms and (min_prime == 0 or p < min_prime):
            min_prime = p
        if count >= k_perms and p > max_prime:
            max_prime = p

    return [len([p for p in prime_counts.keys() if prime_counts[p] >= k_perms]), min_prime, max_prime]

n_max, k_perms = map(int, sys.stdin.readline().split())
print(prime_permutations(n_max, k_perms))

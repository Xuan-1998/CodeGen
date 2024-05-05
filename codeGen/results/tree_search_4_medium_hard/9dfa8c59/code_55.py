import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_permutations_count(n_max, k_perms):
    primes = [i for i in range(2, n_max + 1) if is_prime(i)]
    count = 0
    min_prime = max_prime = None

    for p in primes:
        perms = set(permutations(str(p)))
        if len(perms) == k_perms and all(is_prime(int(''.join(map(str, perm))))) for perm in perms):
            count += 1
            if min_prime is None or p < min_prime:
                min_prime = p
            if max_prime is None or p > max_prime:
                max_prime = p

    return [count, min_prime, max_prime]

n_max, k_perms = map(int, sys.stdin.readline().split())
print(prime_permutations_count(n_max, k_perms))

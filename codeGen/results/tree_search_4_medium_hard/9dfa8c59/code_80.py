from collections import Counter
from math import sqrt, ceil

def prime_permutations(n_max, k_perms):
    if k_perms < 1 or k_perms > 3:
        return [0, 0, 0]

    primes = []
    for i in range(2, n_max + 1):
        is_prime = True
        for j in range(2, ceil(sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    count = 0
    min_prime = n_max
    max_prime = 0

    for prime in primes:
        digits = sorted(str(prime))
        perms = Counter(tuple(digits[i:] + digits[:i]) for i in range(len(digits)))
        if perms[prime] == k_perms:
            count += 1
            min_prime = min(min_prime, prime)
            max_prime = max(max_prime, prime)

    return [count, min_prime, max_prime]

if __name__ == "__main__":
    n_max, k_perms = map(int, input().split())
    print(prime_permutations(n_max, k_perms))

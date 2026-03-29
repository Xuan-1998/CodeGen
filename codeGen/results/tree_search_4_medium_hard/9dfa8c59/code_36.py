import sys
from collections import defaultdict

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [p for p in range(2, n + 1) if sieve[p]]

def permutations(digits):
    if len(digits) == 1:
        return {int(d): 1}
    result = defaultdict(int)
    for i, d in enumerate(sorted(set(str(digits)))):
        perm_len = len(str(digits))
        for p in permutations(d * (perm_len - 1) + '0'):
            for j in range(len(p) - 1):
                result[int(''.join(sorted(str(digits).replace(str(d), str(p[j]))))) + int(p[-1])] += 1
    return result

def solve():
    n_max, k_perms = map(int, input().split())
    primes = sieve_of_eratosthenes(n_max)
    dp = [defaultdict(int) for _ in range(len(str(n_max)))]
    count = min_prime = max_prime = 0
    for i in range(2, n_max + 1):
        if i in primes:
            p_perm_count = permutations(str(i))
            for k, v in p_perm_count.items():
                if k <= k_perms and v > 0:
                    count += 1
                    min_prime = min(min_prime, k) if not min_prime else min_prime
                    max_prime = max(max_prime, k) if not max_prime else max_prime
    print(count, min_prime, max_prime)

if __name__ == '__main__':
    solve()

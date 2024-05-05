import itertools
from collections import defaultdict

def solve():
    n_max, k_perms = map(int, input().split())
    primes = [True] * (n_max + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n_max ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n_max + 1, i):
                primes[j] = False

    prime_perm_count = defaultdict(int)
    smallest_prime = largest_prime = float('inf')

    for p in range(2, n_max + 1):
        if not primes[p]: continue
        perm_count = 0
        for _ in range(k_perms):
            perm = int(''.join(sorted(str(p))))
            if perm <= n_max and primes[perm]:
                perm_count += 1
        prime_perm_count[(p, perm_count)] += 1

    result = [0, float('inf'), -float('inf')]
    for (num, k), count in prime_perm_count.items():
        if k == k_perms:
            result[0] = count
            result[1] = min(result[1], num)
            result[2] = max(result[2], num)

    print(*result)

if __name__ == "__main__":
    solve()

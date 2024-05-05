def solve():
    n_max, k_perms = map(int, input().split())
    primes = [True] * (n_max + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n_max ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n_max + 1, i):
                primes[j] = False

    prime_counts = {}
    smallest_prime = float('inf')
    largest_prime = 0
    count = 0

    for i in range(2, n_max + 1):
        if primes[i]:
            num_str = str(i)
            perms = set()
            for p in permutations(num_str):
                perm_str = int(''.join(p))
                if 2 <= perm_str <= n_max and primes[perm_str]:
                    perms.add(int(''.join(map(str, p))))
            if len(perms) == k_perms:
                prime_counts[i] = len([p for p in perms if primes[p]])
                count += 1
                smallest_prime = min(smallest_prime, i)
                largest_prime = max(largest_prime, i)

    return [count, smallest_prime, largest_prime]

from itertools import permutations

print(solve())

from collections import defaultdict
import sys

def count_prime_permutations(n_max, k_perms):
    primes = []
    is_prime = [True] * (n_max + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n_max ** 0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n_max + 1, p):
                is_prime[i] = False

    for p in range(2, n_max + 1):
        if is_prime[p]:
            primes.append(p)

    dp = defaultdict(bool)
    memo = {}

    def count_permutations(n):
        if n < 10:
            return 1
        if n in memo:
            return memo[n]
        result = 0
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0 and len(str(d)) == len(set(str(d))):
                result += count_permutations(int(''.join(sorted(str(d)))) + 1)
        memo[n] = result
        return result

    for p in primes:
        if count_permutations(p) == k_perms:
            dp[p] = True

    smallest, largest = None, None
    count = sum(1 for p in primes if dp[p])

    for p in primes:
        if dp[p]:
            if smallest is None or p < smallest:
                smallest = p
            if largest is None or p > largest:
                largest = p

    return [count, smallest, largest]

n_max, k_perms = map(int, input().split())
print(*count_prime_permutations(n_max, k_perms), sep='\n')

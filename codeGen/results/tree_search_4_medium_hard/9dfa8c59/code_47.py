from collections import Counter
import heapq

def check_prime_permutations(n, k):
    if n < 2:
        return 0

    prime_perm_count = Counter(str(n)).values().count(1)
    permutations = [int(''.join(map(str, p))) for p in itertools.permutations(str(n))]
    primes = [p for p in permutations if is_prime(p)]
    primes.sort()
    
    left, right = 0, len(primes) - 1
    while k > 0 and left <= right:
        mid = (left + right) // 2
        if primes[mid] == n:
            return prime_perm_count
        elif primes[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
        k -= 1

    return 0


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n_max = int(input())
k_perms = int(input())

dp = [[0] * (k_perms + 1) for _ in range(n_max + 1)]

min_p, max_p = float('inf'), -float('inf')
for p in range(2, n_max + 1):
    if is_prime(p):
        count = check_prime_permutations(p, k_perms)
        dp[p][k_perms] += 1
        min_p = min(min_p, p)
        max_p = max(max_p, p)

answer = [dp[n_max][k_perms], min_p, max_p]
print(*answer, sep='\n')

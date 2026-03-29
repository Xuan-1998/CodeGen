from functools import lru_cache

def max_beauty(n, m, A):
    @lru_cache(None)
    def beauty(i, j):
        bad_primes_in_range = [p for p in primes if p >= A[i] and p <= A[j]]
        return 1 if not bad_primes_in_range else 0

    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if A[i - 1] % A[j - 1] == 0:
                if beauty(i, j):
                    dp[i][j] = max(dp[i-1][j], 1)
                else:
                    dp[i][j] = max(dp[i-1][j], 0)
            else:
                if beauty(i, j):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

    return dp[-1][-1]

def sieve_of_eratosthenes(n):
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

n, m = map(int, input().split())
A = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

primes = sieve_of_eratosthenes(max(A) + 10)

print(max_beauty(n, m, A))

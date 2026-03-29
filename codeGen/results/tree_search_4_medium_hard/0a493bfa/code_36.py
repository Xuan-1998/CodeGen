from math import gcd
import sys

def beauty_of_array():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = set(map(int, input().split()))

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    primes = [i for i in range(2, int(max(a)) + 1) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))]
    good_primes = {p for p in primes if p not in b}

    for i in range(n):
        for j in range(m + 1):
            if a[i] == 1:
                dp[i][j] = 0
            else:
                g = gcd(a[i], max((a[k] for k in range(n) if k != i)))
                if g in good_primes:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + a[i])
                else:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] - a[i])

    return max(max(row) for row in dp)

print(beauty_of_array())

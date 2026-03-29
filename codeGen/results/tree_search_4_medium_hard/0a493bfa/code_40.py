import heapq
from math import gcd

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    memo = {}

    def update_dp(i, j):
        if (i, j) not in memo:
            memo[(i, j)] = max(
                dp[i-1][k-1] - min(bad_primes[j-1], gcd(arr[i], arr[k])) for k in range(1, i+1)) if j > 0 else
                dp[i-1][k-1] + min(arr[i], gcd(arr[i], arr[k])) for k in range(1, i+1))
            dp[i][j] = memo[(i, j)]

    for i in range(n + 1):
        update_dp(i, 0)
        for j in range(m + 1):
            if j > 0:
                update_dp(i, j)

    return max(dp[-1])

print(solve())

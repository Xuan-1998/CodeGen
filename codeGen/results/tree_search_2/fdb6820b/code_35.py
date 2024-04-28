import sys

def count_ways(m, N):
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for k in range(m):
            if i - arr[k] >= 0:
                dp[i] += dp[i - arr[k]]
                dp[i] %= MOD

    return dp[N]

m, N = map(int, input().split())
arr = list(map(int, input().split()))
print(count_ways(m, N))

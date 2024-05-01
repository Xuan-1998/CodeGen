import sys

# Read input from stdin
m, N = map(int, input().split())
arr = list(map(int, input().split()))

mod = 10**9 + 7

dp = [[0] * (m+1) for _ in range(N+1)]

for i in range(m+1):
    dp[0][i] = 1

for N in range(1, N+1):
    for i in range(1, min(N+1, m+1)):
        if N >= arr[i-1]:
            dp[N][i] = (dp[N-arr[i-1]][0] + dp[N][i-1]) % mod
        else:
            dp[N][i] = 0

print(dp[N][m])

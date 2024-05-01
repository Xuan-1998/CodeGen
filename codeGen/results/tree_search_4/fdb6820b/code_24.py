import sys

dp = [[0]*(1005) for _ in range(10005)]

m, N = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(N+1):
    dp[i][0] = 1

for j in range(m+1):
    dp[0][j] = 1

for i in range(1, N+1):
    for k in range(m):
        if arr[k] <= i:
            dp[i][k+1] += dp[i-arr[k]][k]

print(dp[N][m]%1000000007)

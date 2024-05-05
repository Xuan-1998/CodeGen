import sys

n = int(input())
dp = [[-1] * (10**9 + 1) for _ in range(n + 1)]
a = list(map(int, input().split()))

for i in range(2, n + 1):
    for j in range(1, 10**9 + 1):
        if a[i - 1] == j:
            dp[i][j] = max(dp[i-1][j], (dp[i-1][j-a[i]]+a[i])%10**9+1)
        elif i > 2:
            dp[i][j] = min(dp[i-1][j], dp[i-1][a[i]])
        else:
            dp[i][j] = j

for i in range(1, n):
    print(dp[i + 1].index(max(dp[i+1])))

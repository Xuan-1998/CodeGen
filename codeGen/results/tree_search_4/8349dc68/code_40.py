import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(k + 1):
    dp[0][i] = -float('inf')

for i in range(1, n + 1):
    dp[i][0] = max(arr[:i])

for i in range(1, n + 1):
    for j in range(min(i, k) + 1):
        if j == 0:
            dp[i][j] = max(arr[:i])
        else:
            dp[i][j] = max(dp[i-1][j-1] + arr[i-1], dp[i-1][j])

print(max(dp[n]))

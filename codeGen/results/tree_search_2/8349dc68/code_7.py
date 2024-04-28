import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[0] * (k + 1) for _ in range(n)]

for i in range(k):
    dp[i][0] = arr[i]

for i in range(k, n):
    dp[i][0] = max(dp[i-1][0], arr[i])

for j in range(1, k+1):
    for i in range(j, n):
        if j == 1:
            dp[i][j] = max(dp[i-1][0], arr[i])
        else:
            dp[i][j] = max(dp[i-1][min(j, k)], dp[i-j][j-k] + arr[i])

print(max(dp[-1]))

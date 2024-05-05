import sys

n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n):
    dp[i][i] = 0
    for j in range(i - 1, -1, -1):
        if arr[j] >= arr[i]:
            dp[i][j] = dp[i-1][j-1] if j > 0 else 0
        else:
            dp[i][j] = min(dp[i-1][j] + (arr[i] - arr[j] + 1), dp[i-1][j-1] + 2)
        for k in range(j, i):
            dp[i][k] += 1

print(min(dp[-1]))

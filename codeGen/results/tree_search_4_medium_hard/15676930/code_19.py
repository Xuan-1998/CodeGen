import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = c[i - 1]
    for j in range(1, min(i // 2, n)):
        dp[i][j] = max(a[i - 1] + dp[i - 1][j - 1], b[i - 1] + dp[i - 1][j], c[i - 1] + dp[i - 1][j + 1])

print(dp[n][0])

import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, min(i, n) + 1):
        dp[i][j] = max(dp[k][j - 1] + (a[i - k] if k == 0 or c[i - k] else b[i - k]) for k in range(j))

print(dp[n][n])

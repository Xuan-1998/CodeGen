import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[[0] * 2 for _ in range(2)] for _ in range(n)]

for i in range(n):
    if i > 0:
        dp[i][0][1] = max(dp[i-1][1][1], dp[i-1][0][1]) + c[i]
        dp[i][0][0] = max(dp[i-1][1][1], dp[i-1][0][1]) + b[i]
        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0]) + a[i]
        dp[i][1][1] = dp[i-1][1][1] + c[i]

print(max(dp[-1][j][k] for j in range(2) for k in range(2)))

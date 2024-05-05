import sys

n = int(input())
dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for j in range(i):
        if t_j <= t_i:
            dp[i] = min(dp[i], dp[j] + (i - j) * 20)

print(dp[n])

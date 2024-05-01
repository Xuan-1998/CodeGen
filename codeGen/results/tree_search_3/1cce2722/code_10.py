import sys

n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    if a[i - 1] == i:
        dp[i] = dp[i - 1]
    else:
        dp[i] = max(dp[i - 1], dp[i - 2] + a[i])

print(dp[n])

import sys
input()
n, t = map(int, input().split())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], round(10 ** (n - i)) + dp[i - 1])
print(int(dp[-1]))

import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n):
    dp[i] = max(dp[i - 1] + b[i], c[i])
dp[n - 1] += a[-1]

print(max(0, dp[0]) + sum(a))

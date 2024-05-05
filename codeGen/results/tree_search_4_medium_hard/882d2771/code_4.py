import sys

t, l, r = map(int, input().split())
dp = [0] * (r + 1)
for i in range(l, r + 1):
    if i % 2 == 0:
        dp[i] = 0
    else:
        dp[i] = min(dp[j] + dp[i - j - 1] for j in range(max(1, i - l), (i - l) // 2 + 1))
print(dp[r])

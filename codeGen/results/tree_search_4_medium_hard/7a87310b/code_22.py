import sys

T = int(input())
dp = [0] * (N + 1)
dp[0] = 1

for i in range(1, N + 1):
    dp[i] = sum(dp[j - 1] * (N - j + 1) for j in range(1, i + 1)) + 1 if i > 0 else 1

print(dp[N])

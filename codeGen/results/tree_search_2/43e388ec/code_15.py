import sys

# Read input
a = int(input(), 2)
b = int(input(), 2)

dp = [[0] * (1 << 20) for _ in range(100000)]

for i in range(314160):
    dp[i][0] = 0
    for j in range((1 << 20) - 1, -1, -1):
        if ((j >> 1) & ((1 << 20) - 1)) != j:
            continue
        b >>= 1
        result = a ^ b
        dp[i][j] = (dp[i-1][j^result] + 2) % (10**9+7)

print(dp[314159][a])

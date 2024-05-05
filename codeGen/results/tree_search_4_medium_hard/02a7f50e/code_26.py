import sys

n = int(sys.stdin.readline())
dp = [[0] * (1000001) for _ in range(n)]
prev_destroyed = [0] * n

for i in range(n):
    pos, power = map(int, sys.stdin.readline().split())
    prev_destroyed[i] = dp[i][power]

    for j in range(1, 1000001):
        if j <= power:
            dp[i][j] = min(dp[i-1][j], prev_destroyed[i-1] + 1)
        else:
            dp[i][j] = dp[i-1][j]

print(min(dp[-1]))

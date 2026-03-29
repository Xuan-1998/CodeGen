import sys

n = int(input())
marks_above_water = list(map(int, input().split()))

dp = [[0] * (i + 1) for i in range(n + 1)]

for k in range(n + 1):
    dp[0][k] = k * (k + 1) // 2

for i in range(1, n + 1):
    for k in range(i + 1):
        if k == 0:
            dp[i][k] = sum(marks_above_water[:i])
        else:
            dp[i][k] = min(dp[i - j][min(k, j)] + sum(marks_above_water[i - j:i]) for j in range(1, i + 1))

print(min(dp[-1]))

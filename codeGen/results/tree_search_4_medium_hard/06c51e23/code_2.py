===BEGIN CODE===
from math import floor, ceil
t = int(input())  # time limit
n = int(input())  # length of decimal fraction
fraction = [int(i) for i in input().split('.')[1]]  # decimal fraction

dp = [[0.0] * (t + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(min(t, i), -1, -1):  # reverse iteration over time limit
        if floor(fraction[i - 1] / 10.0**j) == ceil(fraction[i - 1] / 10.0**j):  # round down
            dp[i][j] = max(dp[i-1][j-1], fraction[i-1] + dp[i-1][j])
        else:  # round up or not rounding at all
            dp[i][j] = max(dp[i-1][j], fraction[i-1] + dp[i-1][j])

print(f"{dp[n][t]:.6f}" if n > 0 and t > 0 else "0")
===END CODE===

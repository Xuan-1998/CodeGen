import sys

# Read input
n, m, c0, d0 = map(int, input().split())
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = max(dp[i-1][0], 0)   # maximum profit without any stuffing
    for j in range(1, min(i//c0, m)+1):  # iterate over all possible numbers of stuffing types
        if i >= c0 and j > 0:
            dp[i][j] = max(dp[i-c0][j-1], dp[i][j-1]) + d0   # choose the better option: with or without stuffing
        else:
            dp[i][j] = dp[i][j-1]

max_profit = 0
for i in range(n+1):
    if dp[i][m] > max_profit:
        max_profit = dp[i][m]
print(max_profit)

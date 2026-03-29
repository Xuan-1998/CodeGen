import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
max_profit = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # Read the stuffing type's details
        ai, bi, ci, di = map(int, input().split())
        
        # If we don't use this stuffing, our options are:
        # - Use no dough and no stuffing (dp[i][j-1])
        # - Use some dough but no stuffing (dp[i-ci][j])
        dp[i][j] = max(dp[i][j-1], dp[i-ci][j])

        # If we use this stuffing, our options are:
        # - Spend bi grams of stuffing and ci grams of dough
        # - Add di to our profit
        dp[i][j] += min(bi, i) * (di - dp[i-bi][j-1])

max_profit = max(max_profit, dp[n][m])
print(max_profit)

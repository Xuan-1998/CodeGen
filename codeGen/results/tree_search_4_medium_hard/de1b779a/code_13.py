# Initialize dp table with zeros
dp = [[0] * 11 for _ in range(1001)]

# Read input values
n, m, c0, d0 = map(int, input().split())
for i in range(m):
    ai, bi, ci, di = map(int, input().split())

# Fill dp table using memoization
for i in range(n + 1):
    for j in range(min(i // c0, m) + 1):
        if i == 0:
            dp[i][j] = 0
        elif j == 0:
            dp[i][j] = d0 * min(i // c0, m)
        else:
            # Option 1: Do not use any stuffing type
            no_stuffing_profit = d0 * min(i // c0, m)
            # Option 2: Use one of the remaining stuffing types
            using_stuffing_profit = max([dp[max(0, i - ai)][j - 1] + di for ai in range(min(i, bi) + 1)])
            dp[i][j] = max(no_stuffing_profit, using_stuffing_profit)

# Print the maximum profit that can be achieved
print(dp[n][m])

# Read input from stdin
n, m, c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))

# Initialize variables for dynamic programming
dp = [[0] * (d0 + 1) for _ in range(n + 1)]
stuffing_dp = [[0] * (n + 1) for _ in range(m + 1)]

# Fill up the dp table based on whether we use a stuffing or not
for i in range(1, n + 1):
    for j in range(d0 + 1):
        if i <= c0 and j >= ci:
            dp[i][j] = max(dp[i-1][j], di + dp[0][j-ci])
        else:
            dp[i][j] = dp[i-1][j]

# Fill up the stuffing_dp table based on whether we use a certain stuffing or not
for i in range(1, n + 1):
    for j in range(m + 1):
        if j > 0 and i <= ai[j-1]:
            stuffing_dp[i][j] = max(stuffing_dp[i-1][j], bi[j-1] + dp[0][i-bi[j-1]] + di - ci)
        else:
            stuffing_dp[i][j] = stuffing_dp[i-1][j]

# Calculate the maximum profit
max_profit = 0
for i in range(1, n + 1):
    for j in range(m + 1):
        if i <= ai[j-1]:
            max_profit = max(max_profit, dp[i][d0] - ci)

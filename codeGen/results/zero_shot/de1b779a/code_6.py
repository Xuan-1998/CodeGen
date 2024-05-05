# Initialize dp table with zeros
dp = [[0] * (c0 + d0) for _ in range(m + 1)]

for i in range(m + 1):
    for j in range(c0 + d0):
        if i == 0 or j == 0:
            dp[i][j] = 0

# Fill the dp table
for i in range(1, m + 1):
    for j in range(1, c0 + d0):
        ai, bi, ci, di = stuffed_stuffs[i - 1]
        if j < bi:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - bi] + di)

# Find the maximum profit
max_profit = 0
for i in range(c0, c0 + d0):
    if dp[m][i] > max_profit:
        max_profit = dp[m][i]

print(max_profit)

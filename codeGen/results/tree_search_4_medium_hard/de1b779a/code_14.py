n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for j in range(m + 1):
    dp[0][j] = d0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if c0 <= i and j > 0:
            # If the current amount of dough is enough to make a bun with stuffing
            dp[i][j] = max(dp[i - c0][j - 1] + d0, dp[i][j - 1])
        else:
            # If not, we can only sell buns without stuffing
            dp[i][j] = dp[i][j - 1]

print(dp[n][m])

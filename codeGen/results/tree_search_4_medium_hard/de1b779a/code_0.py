# Initialize dp table
n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(m + 1):
        if i == 0 and j > 0:
            dp[i][j] = d0
        elif i > 0 and j > 0:
            # Calculate the maximum profit by either using or not using the current stuffing type
            use_current = dp[i - c0][j - 1] + d0 if c0 <= i else 0
            do_not_use_current = dp[i][j - 1]
            dp[i][j] = max(use_current, do_not_use_current)

print(dp[n][m])

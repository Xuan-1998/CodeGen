import sys

# Read input from stdin
n, m, c0, d0 = map(int, input().split())
dp = [[0, 0, 0] for _ in range(n+1)]
stuffs = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffs.append((ai, bi, ci, di))

# Initialize base cases
dp[0][0] = d0

# Fill up the DP table
for i in range(1, n+1):
    for j in range(min(i+1, m+1)):
        if j == 0:  # Make a bun without any stuffing
            dp[i][j] = max(dp[i-1][j], dp[0][j]) + d0
        else:
            ai, bi, ci, di = stuffs[j-1]
            if i >= ci and ai > 0:  # Make a bun with the current stuffing type
                dp[i][j] = max(dp[i-ci][j-1], dp[0][j]) + di
            else:
                dp[i][j] = dp[i-1][j]

# Print the maximum profit that can be achieved
print(max(dp[n][i] for i in range(m+1)))

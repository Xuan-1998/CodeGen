import sys

# Read input
n, m, c0, d0 = map(int, input().split())
dp = [[-1] * (m + 1) for _ in range(n + 1)]
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))

# Fill dp table
for i in range(c0 + 1):
    for j in range(m + 1):
        if i < c0 and j > 0:
            dp[i][j] = max(dp[i-1][0], dp[max(0, i-ci[j])][max(0, j-1)]) + di[j]
        else:
            if i == c0 and j == 0:
                dp[i][j] = d0
            elif i < c0 and j == 0:
                dp[i][j] = max(dp[max(0, i-1)][0], dp[max(0, i-c0)][0]) + d0
            else:
                dp[i][j] = -float('inf')
        if dp[i][j] < 0:
            dp[i][j] = 0

# Print output
print(dp[n][m])

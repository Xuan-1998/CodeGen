import sys

# Read input from standard input
n, m, c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    a, b, c, d = map(int, input().split())
    stuffings.append((a, b, c, d))

# Initialize the dynamic programming table
dp = [[0] * (m + 1) for _ in range(n + 1)]

# Fill up the dynamic programming table
for i in range(1, n + 1):
    for j in range(m + 1):
        if i < c0 or j == 0:
            dp[i][j] = dp[i][j - 1]
        else:
            without_stuffing = d0
            with_stuffing = dp[i - c0][j - 1] + d
            dp[i][j] = max(without_stuffing, with_stuffing)

# Print the maximum profit that can be achieved
print(dp[-1][-1])

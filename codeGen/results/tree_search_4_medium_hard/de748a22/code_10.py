import sys

# Read input and initialize DP table
n, q = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(n + 1)]
signs = list(input())

# Precompute prefix sums
prefix_sums = [0]
for i in range(1, n + 1):
    if signs[i - 1] == "+":
        prefix_sums.append(prefix_sums[-1] + 1)
    else:
        prefix_sums.append(prefix_sums[-1] - 1)

# Initialize DP table
for i in range(n + 1):
    dp[i][0] = 0

# Fill up the DP table
for i in range(1, n + 1):
    for j in range(i + 1):
        if signs[j - 1] == "+":
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + (i - j))
        else:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] - (i - j))

# Process queries
for _ in range(q):
    l, r = map(int, input().split())
    print(min(dp[r][l - 1], dp[l - 1][r]))

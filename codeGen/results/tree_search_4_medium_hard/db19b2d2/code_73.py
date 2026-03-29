import sys

# Read input
n, m, h = map(int, input().split())
dept_sizes = list(map(int, input().split()))

# Initialize 2D table for dynamic programming
dp = [[0.0] * (n + 1) for _ in range(m + 1)]

# Fill up the dp table
for i in range(1, m + 1):
    for j in range(n + 1):
        if j == 0:
            dp[i][j] = 0.0
        elif i < h:
            dp[i][j] = 1.0
        else:
            # Calculate the probability that at least one player from department i is selected
            # This is calculated as 1 - (1 - (dept_sizes[i - 1] / sum(dept_sizes))**j) for j > 0, and 1 for j = 0
            if j == 0:
                dp[i][j] = 1.0
            else:
                dp[i][j] = 1 - (1 - (dept_sizes[i - 1] / sum(dept_sizes))**j)

# Print the result
ans = max(0, min(1, 1 - dp[h][n]))
print("{:.6f}".format(ans))

import sys

# Read input from stdin
n, m = map(int, input().split())

# Create a 2D array dp of size (n+1) x (m+1)
dp = [[0] * (m + 1) for _ in range(n + 1)]

# Fill up the base case: when either i or j is equal to 1
for i in range(n + 1):
    dp[i][1] = 1
for j in range(m + 1):
    dp[1][j] = 1

# Iterate over all possible rectangles of size i x j, and fill up the dp array
for i in range(2, n + 1):
    for j in range(2, m + 1):
        # Consider all possible ways to tile the rectangle by placing a square of size k x k at the top-left corner
        for k in range(min(i, j), 0, -1):
            if i % k == 0 and j % k == 0:
                # Calculate the remaining area that needs to be tiled: (i-k) x (j-k)
                dp[i][j] = min(dp[i][j], dp[i - k][j - k] + 1)
                break

# Return dp[n][m] as the result, which represents the minimum number of integer-sided squares that tile the given rectangle
print(dp[n][m])

from sys import stdin

# Read input from standard input
n, m = map(int, stdin.readline().split())

# Initialize a 2D array to store the results of subproblems
dp = [[0] * (m + 1) for _ in range(n + 1)]

# Base case: a single unit square can always tile a rectangle of size 1 x j
for j in range(m + 1):
    dp[1][j] = 1

# Transition relationship: the minimum number of squares that tile a rectangle of size i x j is the minimum of:
# - The minimum number of squares that tile a rectangle of size (i-1) x k, plus the minimum number of squares that tile a rectangle of size 1 x (j-k)
for i in range(2, n + 1):
    for j in range(i, m + 1):
        dp[i][j] = min(dp[i-1][k]+dp[1][j-k] for k in range(1, j+1))

# Print the result
print(dp[n][m])

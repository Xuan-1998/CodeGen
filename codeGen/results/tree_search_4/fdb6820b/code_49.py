import sys

# Read input from stdin
m, N = map(int, input().split())
arr = list(map(int, input().split()))

# Initialize DP table
dp = [[0] * (N + 1) for _ in range(m + 1)]

# Fill the DP table
for i in range(1, m + 1):
    dp[i][0] = 1
    for j in range(1, N + 1):
        if i <= j:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j-i]) % (10**9 + 7)
        else:
            dp[i][j] = 0

# Print the answer
print(dp[m][N])

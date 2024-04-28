import sys

# Read input values
a, b = map(int, input().split())
mod = 10**9 + 7

# Initialize DP table
dp = [[0] * (20 + 1) for _ in range(31)]

# Fill up the DP table
for i in range(1, 32):
    dp[i][0] = ((a >> (i - 1)) & 1) * ((b >> (i - 1)) & 1)
    for j in range(1, i + 1):
        dp[i][j] = (dp[i-1][0] if j == 0 else dp[i-1][j]) + (a & 1) * (b >> (i - 1))

# Calculate the final result
result = 0
for i in range(32):
    result = (result + dp[31][i]) % mod

print(result)

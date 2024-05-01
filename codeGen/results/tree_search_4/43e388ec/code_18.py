import sys

# Read input from stdin
a = int(input())
b = int(input())

# Initialize dynamic programming table with zeros
dp = [0] * (314160)

# Base case: dp[0] = 0
dp[0] = 0

# Calculate cumulative sums of OR operations
for i in range(1, 314160):
    dp[i] = (a ^ ((b >> (i % 31)) & 1)) + dp[(i - 1) % 31]
    dp[i] %= 10**9 + 7

# Print the final answer modulo 10^9+7
print(dp[-1])

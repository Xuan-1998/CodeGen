import sys

# Read input from stdin
a = int(input(), 2)
b = int(input(), 2)

# Initialize the dp array with zeros
dp = [[0] * (30 + 1) for _ in range(17)]

# Compute the sum modulo 10^9+7 for all values of i
for i in range(1, 314162):
    for j in range(min(i.bit_length(), 29), -1, -1):
        dp[i][j] = (a >> j) ^ b & ((1 << (j + 1)) - 1)
        if i >= 2:
            dp[i][j] += dp[i-1][0]
        dp[i][j] %= int(10**9 + 7)

# Print the final answer
print(sum(dp[314162][i] for i in range(30 + 1)) % (10**9 + 7))

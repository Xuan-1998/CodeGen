import sys

# Read input from stdin
a = int(input(), 2)
b = int(input(), 2)

# Create a 2D array to store the dynamic programming values
dp = [[0] * (len(bin(b)) - 1) for _ in range(len(bin(a)) - 1)]

# Fill up the dp array based on the state expression
for i in range(1, len(bin(a)) - 1):
    for j in range(1, len(bin(b)) - 1):
        # Compute the value of dp[i][j] based on the current bits of a and b
        if (a >> i) & 1 and (b >> j) & 1:
            dp[i][j] = (dp[i-1][j-1] + 1) % (10**9 + 7)
        elif ((a >> i) & 1 or (b >> j) & 1):
            dp[i][j] = (dp[i-1][j-1] + 2) % (10**9 + 7)
        else:
            dp[i][j] = dp[i-1][j-1]

# Compute the final result by adding up the precomputed values in dp[]
result = sum(sum(dp[i]) for i in range(len(bin(a)) - 1))

print(result % (10**9 + 7))

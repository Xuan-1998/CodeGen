import sys

# Read input values
n = int(sys.stdin.readline())
p = [int(x) for x in sys.stdin.readline().split()]

# Initialize a list to store the minimum number of portal moves for each room
dp = [0] * (n + 1)

# Calculate the minimum number of portal moves for each room
for i in range(2, n + 1):
    dp[i] = min(dp[p[i - 1]] + 1, dp[max(i // 2, 1)] + (i % 2))

# Print the result modulo 10^9+7
print((dp[n] + n) % (10**9 + 7))

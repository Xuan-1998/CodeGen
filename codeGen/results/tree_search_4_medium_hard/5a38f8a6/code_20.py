import math

def minPerfectSquares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            if i >= j:
                dp[i] = min(dp[i], dp[j] * 2 + (i - j))
    return dp[n]

# Read input from stdin
n = int(input())

# Calculate and print the result to stdout
print(minPerfectSquares(n))

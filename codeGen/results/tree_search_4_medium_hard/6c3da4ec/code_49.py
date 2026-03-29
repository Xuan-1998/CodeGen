import sys

def max_bitwise_or(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize base cases
    for i in range(n):
        dp[i][i] = int(s[i], 2)

    # Fill up the DP array by iterating from bottom-up
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length
            max_or = 0
            for k in range(i, j):
                dp[i][j] = max(dp[i][j], dp[i][k] | int(s[k+1:j+1], 2))
            if i == 0:
                dp[i][j] += int(s[0:j+1], 2)

    # Find the maximum value
    max_or = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            max_or = max(max_or, dp[i][j])

    return bin(max_or)[2:]

# Read input from stdin
n = int(input())
s = input()

print(max_bitwise_or(s))

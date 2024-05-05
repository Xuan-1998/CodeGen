import sys

def max_bitwise_or(s):
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n)]

    # Base case: when j-i is 0 or 1, there's only one way to pair these substrings
    for j in range(1, n+1):
        dp[0][j] = s[j-1]

    # Fill in the DP table
    for i in range(n):
        for j in range(i+1, n+1):
            max_or = 0
            for k in range(i, j):
                or_val = (s[k] << (j-k)) | dp[i][k]
                if or_val > max_or:
                    max_or = or_val
            dp[i][j] = max_or

    # Find the maximum bitwise OR value
    max_or = 0
    for i in range(n):
        for j in range(i+1, n+1):
            or_val = (s[j-1] << (j-i)) | dp[i][j]
            if or_val > max_or:
                max_or = or_val

    return bin(max_or)[2:]

# Receive input from stdin
n = int(input())
s = input()

print(max_bitwise_or(s))

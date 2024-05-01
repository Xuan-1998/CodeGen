from collections import defaultdict

def max_common_substrings(str1, str2):
    n = len(str1)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Initialize the DP table with base cases
    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1

    # Fill up the DP table using memoization
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

    # Return the maximum value in the DP table
    return max(max(row) for row in dp)

# Read input from standard input
str1, str2 = input().split()

# Print the output to standard output
print(max_common_substrings(str1, str2))

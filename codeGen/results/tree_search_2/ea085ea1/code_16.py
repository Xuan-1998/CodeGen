def max_common_substrings(str1, str2):
    n = len(str1)
    m = len(str2)

    # Initialize DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The maximum number of common non-overlapping substrings is stored in the last cell
    return dp[n][m]

# Read input strings from standard input
str1 = input()
str2 = input()

# Calculate and print the result
result = max_common_substrings(str1, str2)
print(result)

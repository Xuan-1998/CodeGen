def max_common_substrings(str1, str2):
    n = len(str1)
    m = len(str2)

    # Initialize the DP table with zeros
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the DP table using dynamic programming and memoization
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Find the maximum number of common non-overlapping substrings
    max_len = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if dp[i][j] > max_len:
                max_len = dp[i][j]

    return max_len

# Read input from stdin and print the answer to stdout
str1 = input()
str2 = input()

print(max_common_substrings(str1, str2))

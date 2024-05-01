def max_common_substrings(str1, str2):
    n = len(str1)
    m = len(str2)

    # Initialize dp table with zeros
    dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(n + 1)]

    # Fill up the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j][0] = dp[i - 1][j - 1][0] + 1
            else:
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0])

    # Backtrack to find the maximum number of common non-overlapping substrings
    i, j, k = n, m, dp[n][m][0]
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            i -= 1
            j -= 1
            k -= 1
        elif k == dp[i - 1][j][0]:
            i -= 1
        else:
            j -= 1

    return k


# Read input from standard input
str1 = input()
str2 = input()

# Calculate the maximum number of common non-overlapping substrings and print the result to standard output
print(max_common_substrings(str1, str2))
